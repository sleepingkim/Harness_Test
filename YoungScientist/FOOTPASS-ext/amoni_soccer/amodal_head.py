"""Module 1: Soccer-Amodal Head.

Given per-player RoI features, predicts three masks (visible, amodal, occlusion)
and an amodal uncertainty score. Designed to be finetuned from SAMEO-generated
pseudo-labels on SoccerNet.

Reference: 05_research_design.md §4.2
Key outputs:
    M_vis  (B*M*T, 1, 56, 56)   visible mask
    M_amo  (B*M*T, 1, 56, 56)   amodal mask (full shape, including occluded)
    M_occ  (B*M*T, 1, 56, 56)   occlusion mask = max(0, M_amo - M_vis)
    u_a    (B*M*T,)             amodal uncertainty scalar in [0, 1]
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


def _conv_bn_act(in_c: int, out_c: int, k: int = 3) -> nn.Module:
    return nn.Sequential(
        nn.Conv2d(in_c, out_c, kernel_size=k, padding=k // 2, bias=False),
        nn.BatchNorm2d(out_c),
        nn.GELU(),
    )


class _MaskDecoder(nn.Module):
    """Small decoder: 4 conv blocks + upsample to 56x56 logits."""

    def __init__(self, in_channels: int = 192):
        super().__init__()
        self.block1 = _conv_bn_act(in_channels, 128)
        self.block2 = _conv_bn_act(128, 96)
        self.up1 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)  # 14->28
        self.block3 = _conv_bn_act(96, 64)
        self.up2 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)  # 28->56
        self.block4 = _conv_bn_act(64, 32)
        self.out = nn.Conv2d(32, 1, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.block1(x)
        x = self.block2(x)
        x = self.up1(x)
        x = self.block3(x)
        x = self.up2(x)
        x = self.block4(x)
        return self.out(x)  # logits, no sigmoid here


class SoccerAmodalHead(nn.Module):
    """UOAIS-style hierarchical amodal head adapted to soccer players.

    Inputs:
        roi_feat: (N, C, H, W) where N = B*M*T (typically C=192, H=W=14 from RoIAlign)
        pose_prior: optional (N, 17, H, W) pose keypoint heatmaps
    Outputs dict with:
        m_vis, m_amo, m_occ: (N, 1, 56, 56) sigmoid-activated masks in [0,1]
        m_vis_logits, m_amo_logits: (N, 1, 56, 56) raw logits (for BCE loss)
        u_a: (N,) amodal uncertainty scalar in [0,1]
    """

    def __init__(self, in_channels: int = 192, use_pose_prior: bool = True,
                 pose_channels: int = 17):
        super().__init__()
        self.use_pose_prior = use_pose_prior
        self.pose_channels = pose_channels

        vis_in = in_channels + (pose_channels if use_pose_prior else 0)
        self.visible_decoder = _MaskDecoder(in_channels=vis_in)
        self.amodal_decoder = _MaskDecoder(in_channels=vis_in)

        # Uncertainty head: global pooled RoI feature -> u_a
        self.u_pool = nn.AdaptiveAvgPool2d(1)
        self.u_mlp = nn.Sequential(
            nn.Linear(in_channels, 64),
            nn.GELU(),
            nn.Linear(64, 1),
        )

    @staticmethod
    def _mask_entropy(mask_prob: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
        """Pixel-wise binary entropy, averaged per sample."""
        p = mask_prob.clamp(eps, 1 - eps)
        ent = -(p * torch.log(p) + (1 - p) * torch.log(1 - p))
        return ent.mean(dim=(-1, -2, -3))  # (N,)

    def forward(self, roi_feat: torch.Tensor,
                pose_prior: torch.Tensor | None = None) -> dict:
        N, C, H, W = roi_feat.shape

        if self.use_pose_prior:
            if pose_prior is None:
                # If caller did not provide pose, pass zeros — the model can still run
                pose_prior = torch.zeros(N, self.pose_channels, H, W,
                                         device=roi_feat.device, dtype=roi_feat.dtype)
            fused = torch.cat([roi_feat, pose_prior], dim=1)
        else:
            fused = roi_feat

        vis_logits = self.visible_decoder(fused)
        amo_logits = self.amodal_decoder(fused)

        m_vis = torch.sigmoid(vis_logits)
        m_amo = torch.sigmoid(amo_logits)
        # Consistency: amodal should cover visible
        m_occ = torch.clamp(m_amo - m_vis, min=0.0)

        # Uncertainty: learned scalar + entropy-based regularizer
        pooled = self.u_pool(roi_feat).flatten(1)  # (N, C)
        u_learned = torch.sigmoid(self.u_mlp(pooled)).squeeze(-1)  # (N,)
        # Optional: entropy component (not added during training loss, used at inference)
        u_entropy = self._mask_entropy(m_amo) - self._mask_entropy(m_vis)
        u_entropy = torch.sigmoid(u_entropy)  # bound to [0,1]
        u_a = 0.5 * u_learned + 0.5 * u_entropy

        return {
            "m_vis": m_vis,
            "m_amo": m_amo,
            "m_occ": m_occ,
            "m_vis_logits": vis_logits,
            "m_amo_logits": amo_logits,
            "u_a": u_a,
            "u_learned": u_learned,
            "u_entropy": u_entropy,
        }


# ------------------------- Loss helpers -------------------------

def amodal_bce_dice_loss(logits: torch.Tensor, target: torch.Tensor,
                         dice_weight: float = 1.0) -> torch.Tensor:
    """BCE + Dice loss for mask prediction."""
    bce = F.binary_cross_entropy_with_logits(logits, target)
    probs = torch.sigmoid(logits)
    num = 2 * (probs * target).sum(dim=(-1, -2, -3))
    den = probs.sum(dim=(-1, -2, -3)) + target.sum(dim=(-1, -2, -3)) + 1e-6
    dice = 1 - (num / den).mean()
    return bce + dice_weight * dice


def consistency_loss(m_vis: torch.Tensor, m_amo: torch.Tensor) -> torch.Tensor:
    """Enforce M_amo >= M_vis pixel-wise. Penalize negative gap."""
    gap = (m_vis - m_amo).clamp(min=0.0)  # positive where m_vis > m_amo (violation)
    return gap.mean()


def uncertainty_calibration_loss(u_a: torch.Tensor,
                                 iou: torch.Tensor) -> torch.Tensor:
    """Force u_a to approximate (1 - IoU) — high uncertainty when mask is bad."""
    target = 1.0 - iou.clamp(0.0, 1.0)
    return F.l1_loss(u_a, target)


def total_amodal_loss(
    head_out: dict,
    gt_vis: torch.Tensor,
    gt_amo: torch.Tensor,
    iou: torch.Tensor | None = None,
    lambda_cons: float = 0.5,
    lambda_u: float = 0.3,
) -> tuple[torch.Tensor, dict]:
    """Combine all amodal losses per §4.2.3 of the research design."""
    L_vis = amodal_bce_dice_loss(head_out["m_vis_logits"], gt_vis)
    L_amo = amodal_bce_dice_loss(head_out["m_amo_logits"], gt_amo)
    gt_occ = torch.clamp(gt_amo - gt_vis, min=0.0)
    # Re-use sigmoid probabilities for occlusion (no separate logits)
    L_occ = F.l1_loss(head_out["m_occ"], gt_occ)
    L_cons = consistency_loss(head_out["m_vis"], head_out["m_amo"])

    total = L_vis + L_amo + L_occ + lambda_cons * L_cons
    breakdown = {"L_vis": L_vis.item(), "L_amo": L_amo.item(),
                 "L_occ": L_occ.item(), "L_cons": L_cons.item()}

    if iou is not None:
        L_u = uncertainty_calibration_loss(head_out["u_a"], iou)
        total = total + lambda_u * L_u
        breakdown["L_u"] = L_u.item()

    breakdown["L_total"] = total.item()
    return total, breakdown

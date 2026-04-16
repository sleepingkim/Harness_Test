"""Extended TAAD: FOOTPASS X3D_TAAD_Baseline wrapper with continuous visibility
and amodal uncertainty injection.

The original FOOTPASS TAAD consumes:
    (x, roi, mask)     where mask is binary {0,1}

This wrapper replaces `mask` with a continuous two-channel signal:
    mask_cont = [visibility, 1 - u_amodal]    ∈ [0,1]^{B x M x T x 2}

and gates the TAAD backbone accordingly, while keeping the upstream repository
untouched. If the amodal head is disabled (config: amodal.enabled=False), the
wrapper degenerates to the original binary TAAD behavior.

Reference: 05_research_design.md §4.1, notes/integration_plan.md
"""
from __future__ import annotations

from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.ops import roi_align

from .amodal_head import SoccerAmodalHead
from .footpass_loader import load_taad_baseline


class ExtendedTAAD(nn.Module):
    """AmoUni-SoccerTrack wrapper around FOOTPASS X3D_TAAD_Baseline.

    The wrapper keeps the original baseline intact and only overrides the
    `mask` multiplication step (line 65 of FOOTPASS-main/models/model_TAAD_baseline.py).

    Forward input signature mirrors FOOTPASS:
        x:   (B, 3, T, 352, 640)
        roi: (B, M, T, 5)
        mask_binary: (B, M, T)  — original binary visibility, used as fallback

    Additional config:
        use_amodal (bool): enable amodal head; default True
        use_uncertainty (bool): combine (1-u_a) into the soft mask; default True
    """

    def __init__(self, use_amodal: bool = True, use_uncertainty: bool = True,
                 amodal_channels: int = 192,
                 pose_channels: int = 17):
        super().__init__()
        self.use_amodal = use_amodal
        self.use_uncertainty = use_uncertainty

        # Load the original FOOTPASS TAAD baseline
        X3D_TAAD_Baseline = load_taad_baseline()
        self.taad = X3D_TAAD_Baseline()

        if self.use_amodal:
            self.amodal_head = SoccerAmodalHead(
                in_channels=amodal_channels,
                use_pose_prior=True,
                pose_channels=pose_channels,
            )
        else:
            self.amodal_head = None

    # ------------------------------------------------------------------
    # We replicate TAAD's forward manually so we can inject our amodal gate.
    # Original logic copied structurally from FOOTPASS-main; we only change
    # how `mask` is applied.
    # ------------------------------------------------------------------
    def _taad_backbone(self, x: torch.Tensor) -> torch.Tensor:
        """Run the X3D backbone up to line 50 of the original forward."""
        taad = self.taad
        w = taad.x3d_L4(x)                     # (B, 48, T, 88, 160)
        z = taad.x3d.blocks[2](w)              # (B, 48, T, 44, 80)
        y = taad.x3d.blocks[3](z)              # (B, 96, T, 22, 40)
        x = taad.x3d.blocks[4](y)              # (B, 192, T, 11, 20)
        x = taad.up_L32(x)                     # (B, 192, T, 22, 40)
        x = torch.cat((x, y), dim=1)           # (B, 288, T, 22, 40)
        x = taad.conv_L16_32(x)                # (B, 192, T, 22, 40)
        x = F.gelu(taad.bn_L16_32(x))
        x = taad.up_L16(x)                     # (B, 192, T, 44, 80)
        x = torch.cat((x, z), dim=1)           # (B, 240, T, 44, 80)
        x = taad.conv_L8_16(x)                 # (B, 192, T, 44, 80)
        x = F.gelu(taad.bn_L8_16(x))
        return x                               # (B, 192, T, 44, 80)

    def _apply_roi_align(self, feat: torch.Tensor, roi: torch.Tensor,
                         B: int, L: int, M: int) -> torch.Tensor:
        """Mirror the RoI align call of the original baseline.

        Args:
            feat: (B, 192, T, 44, 80) backbone features
            roi:  (B, M, T, 5)
        Returns:
            roi_feat: (B*T*M, 192, 4, 2)
        """
        _, _, _, fh, fw = feat.shape
        feat_flat = feat.permute(0, 2, 1, 3, 4).reshape(-1, 192, fh, fw)  # (B*T, 192, fh, fw)

        roi = roi.clone()
        roi = roi.permute(0, 2, 1, 3).reshape(-1, 5)  # (B*T*M, 5)
        f_num = roi[:, 0]
        device = feat.device
        batch_indices = torch.arange(B, device=device).repeat_interleave(L * M)
        adjusted_frame_numbers = f_num + batch_indices * L
        roi[:, 0] = adjusted_frame_numbers

        roi_feat = roi_align(feat_flat, roi, (4, 2), 0.125)  # (B*T*M, 192, 4, 2)
        return roi_feat

    def _compute_soft_mask(self, roi_feat: torch.Tensor,
                           mask_binary: torch.Tensor,
                           B: int, M: int, T: int,
                           pose_prior: Optional[torch.Tensor] = None) -> tuple[torch.Tensor, dict]:
        """Compute continuous visibility mask using amodal head, fallback to binary.

        Returns:
            soft_mask: (B, M, T) in [0,1]
            extras: dict with amodal outputs (for downstream losses)
        """
        extras: dict = {}
        if not self.use_amodal or self.amodal_head is None:
            return mask_binary.float(), extras

        # roi_feat: (B*T*M, 192, 4, 2) — but amodal head expects (N, 192, H, W) with H>=14
        # Upsample to 14x14 to match UOAIS decoder expectation
        N = roi_feat.shape[0]
        roi_feat_up = F.interpolate(roi_feat, size=(14, 14), mode="bilinear",
                                     align_corners=False)

        head_out = self.amodal_head(roi_feat_up, pose_prior=pose_prior)

        # visibility = area(M_vis) / area(M_amo) per sample, in [0,1]
        area_vis = head_out["m_vis"].sum(dim=(-1, -2, -3))  # (N,)
        area_amo = head_out["m_amo"].sum(dim=(-1, -2, -3)).clamp(min=1.0)
        visibility = (area_vis / area_amo).clamp(0.0, 1.0)   # (N,)

        u_a = head_out["u_a"]  # (N,)
        if self.use_uncertainty:
            soft = visibility * (1.0 - u_a)
        else:
            soft = visibility

        # Reshape back: N = B*T*M  ->  (B, M, T)
        soft = soft.reshape(B, T, M).permute(0, 2, 1)  # (B, M, T)
        # Intersect with binary mask so that frames where the player is truly absent
        # (no RoI in the dataset) remain zero even if amodal head hallucinates.
        soft = soft * mask_binary.float()

        extras.update({
            "m_vis": head_out["m_vis"],
            "m_amo": head_out["m_amo"],
            "m_occ": head_out["m_occ"],
            "u_a": u_a,
            "visibility": visibility,
            "soft_mask_BMT": soft,
        })
        return soft, extras

    def _taad_head(self, roi_feat: torch.Tensor, soft_mask: torch.Tensor,
                   B: int, M: int, T: int) -> torch.Tensor:
        """Mirror the RoI -> classification head (lines 63-70 of original)."""
        taad = self.taad
        # (B*T*M, 192, 4, 2) -> (B*M, 192, T)
        x = taad.avgpool2D(roi_feat).squeeze(-1).squeeze(-1)      # (B*T*M, 192)
        x = x.reshape(B, T, M, 192).permute(0, 2, 3, 1)            # (B, M, 192, T)
        x = x.reshape(B * M, 192, T)

        mask_flat = soft_mask.reshape(B * M, T).unsqueeze(1)       # (B*M, 1, T)
        x = x * mask_flat
        x = F.gelu(taad.bn1(taad.conv1(x)))                        # (B*M, 512, T)
        x = taad.fc1(x.permute(0, 2, 1))                           # (B*M, T, 9)
        return x.reshape(B, M, T, 9).permute(0, 3, 1, 2)           # (B, 9, M, T)

    def forward(self, x: torch.Tensor, roi: torch.Tensor,
                mask_binary: torch.Tensor,
                pose_prior: Optional[torch.Tensor] = None,
                return_extras: bool = False):
        """Forward pass.

        Args:
            x:           (B, 3, T, 352, 640)
            roi:         (B, M, T, 5)
            mask_binary: (B, M, T) original FOOTPASS visibility mask
            pose_prior:  optional (B*T*M, 17, 14, 14) pose heatmaps per RoI
            return_extras: if True, also return amodal head outputs for losses

        Returns:
            logits: (B, 9, M, T)  — action class logits matching FOOTPASS TAAD
            extras (optional): dict with amodal predictions and soft mask
        """
        B, _, T, _, _ = x.shape
        _, M, _, _ = roi.shape

        feat = self._taad_backbone(x)                       # (B, 192, T, 44, 80)
        roi_feat = self._apply_roi_align(feat, roi, B, T, M)  # (B*T*M, 192, 4, 2)

        soft_mask, extras = self._compute_soft_mask(
            roi_feat, mask_binary, B, M, T, pose_prior=pose_prior
        )

        logits = self._taad_head(roi_feat, soft_mask, B, M, T)

        if return_extras:
            return logits, extras
        return logits


def load_pretrained_taad_weights(extended_model: ExtendedTAAD, ckpt_path: str) -> None:
    """Load FOOTPASS TAAD baseline weights into the wrapped model.

    Only keys matching 'taad.*' are loaded, leaving the amodal head randomly
    initialized (intended for Stage-2 training).
    """
    state = torch.load(ckpt_path, map_location="cpu")
    if "state_dict" in state:
        state = state["state_dict"]
    taad_state = {k[len("taad."):] if k.startswith("taad.") else k: v
                  for k, v in state.items()}
    missing, unexpected = extended_model.taad.load_state_dict(taad_state, strict=False)
    print(f"[load_pretrained_taad_weights] missing={len(missing)} unexpected={len(unexpected)}")

"""Module 2: Uniform-aware Re-ID.

Addresses research gap ②: same-team players look alike -- appearance alone
fails to discriminate under occlusion. We combine (a) part-based embedding,
(b) pose-guided visibility, (c) jersey-region branch, (d) intra-team contrastive loss.

Reference: 05_research_design.md §4.3
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class UniformAwareReID(nn.Module):
    """Produces (appearance embedding, jersey-region embedding) from RoI features.

    Inputs:
        roi_feat: (N, C, H, W)  player RoI feature
        pose_visibility: optional (N, K) keypoint visibility mask in [0,1]
    Outputs dict:
        f_appearance: (N, D)    L2-normalized global embedding
        f_jersey:     (N, D_j)  L2-normalized jersey-region embedding
        u_r:          (N,)      Re-ID uncertainty scalar in [0,1]
    """

    def __init__(self, in_channels: int = 192, embed_dim: int = 128,
                 jersey_dim: int = 64, num_parts: int = 3):
        super().__init__()
        self.num_parts = num_parts  # upper / middle / lower (horizontal stripes)

        # Part-based embedding: split spatial into `num_parts` stripes
        self.part_pool = nn.AdaptiveAvgPool2d((num_parts, 1))
        self.part_proj = nn.Sequential(
            nn.Linear(in_channels * num_parts, 256),
            nn.BatchNorm1d(256),
            nn.GELU(),
            nn.Linear(256, embed_dim),
        )

        # Jersey-region branch: attention-pool over back-upper region
        # We approximate back-upper as the middle stripe (row-wise center)
        self.jersey_attn = nn.Conv2d(in_channels, 1, kernel_size=1)
        self.jersey_proj = nn.Sequential(
            nn.Linear(in_channels, 128),
            nn.BatchNorm1d(128),
            nn.GELU(),
            nn.Linear(128, jersey_dim),
        )

        # Uncertainty head
        self.u_proj = nn.Sequential(
            nn.Linear(in_channels, 64),
            nn.GELU(),
            nn.Linear(64, 1),
        )

    def forward(self, roi_feat: torch.Tensor,
                pose_visibility: torch.Tensor | None = None) -> dict:
        N, C, H, W = roi_feat.shape

        # Part-based global embedding
        parts = self.part_pool(roi_feat).flatten(1)  # (N, C*num_parts)
        f_app = self.part_proj(parts)
        f_app = F.normalize(f_app, dim=-1)

        # Optional: zero-out invisible parts using pose visibility
        if pose_visibility is not None:
            # pose_visibility: (N, num_parts) expected; reshape if (N, K) keypoints
            if pose_visibility.shape[-1] != self.num_parts:
                # Simple aggregation: split K keypoints into num_parts groups
                K = pose_visibility.shape[-1]
                chunks = torch.chunk(pose_visibility, self.num_parts, dim=-1)
                pose_visibility = torch.stack([c.mean(-1) for c in chunks], dim=-1)
            # Scale embedding by mean visibility
            vis_mean = pose_visibility.mean(-1, keepdim=True)
            f_app = f_app * vis_mean

        # Jersey-region branch (attention pool over back region)
        attn = torch.sigmoid(self.jersey_attn(roi_feat))  # (N,1,H,W)
        pooled = (roi_feat * attn).sum(dim=(-1, -2)) / (attn.sum(dim=(-1, -2)) + 1e-6)  # (N,C)
        f_jersey = self.jersey_proj(pooled)
        f_jersey = F.normalize(f_jersey, dim=-1)

        # Uncertainty: high when attention is diffuse or embedding is ambiguous
        global_pool = roi_feat.mean(dim=(-1, -2))  # (N, C)
        u_r = torch.sigmoid(self.u_proj(global_pool)).squeeze(-1)

        return {
            "f_appearance": f_app,
            "f_jersey": f_jersey,
            "u_r": u_r,
            "attn_map": attn,
        }


# ------------------------- Loss helpers -------------------------

def intra_team_contrastive_loss(
    embeddings: torch.Tensor,
    identities: torch.Tensor,
    teams: torch.Tensor,
    temperature: float = 0.1,
) -> torch.Tensor:
    """Intra-team contrastive loss: pull same identity, push other identities **within the same team**.

    This is stronger than standard contrastive which treats all other identities as negatives.
    Here we emphasize same-team negatives because they share the uniform color.

    Args:
        embeddings: (N, D) L2-normalized embeddings.
        identities: (N,) integer player identities.
        teams:      (N,) integer team ids.

    Returns:
        scalar loss.
    """
    N, D = embeddings.shape
    sim = embeddings @ embeddings.T / temperature  # (N,N)

    # Positive mask: same identity, different index
    pos_mask = (identities.unsqueeze(0) == identities.unsqueeze(1)).float()
    pos_mask.fill_diagonal_(0)

    # Negative mask: same team but different identity (hardest case)
    same_team = (teams.unsqueeze(0) == teams.unsqueeze(1)).float()
    neg_mask_intra = same_team * (1 - pos_mask)
    neg_mask_intra.fill_diagonal_(0)

    # Also include inter-team negatives (softer)
    neg_mask_inter = (1 - same_team)

    # Compose denominator: weight intra-team negatives more
    exp_sim = torch.exp(sim)
    pos_term = (exp_sim * pos_mask).sum(dim=1)
    neg_term = (exp_sim * (neg_mask_intra * 2.0 + neg_mask_inter)).sum(dim=1)

    # Avoid degenerate samples without positives
    has_pos = pos_mask.sum(dim=1) > 0
    if has_pos.sum() == 0:
        return torch.tensor(0.0, device=embeddings.device)

    loss = -torch.log((pos_term[has_pos] + 1e-6) / (pos_term[has_pos] + neg_term[has_pos] + 1e-6))
    return loss.mean()


def uniform_reid_total_loss(
    reid_out: dict,
    identities: torch.Tensor,
    teams: torch.Tensor,
    gt_jersey: torch.Tensor | None = None,
    lambda_intra: float = 1.0,
    lambda_jersey: float = 0.5,
) -> tuple[torch.Tensor, dict]:
    """Composite Re-ID loss per §4.3 of the research design."""
    L_intra = intra_team_contrastive_loss(reid_out["f_appearance"], identities, teams)
    breakdown = {"L_intra": L_intra.item()}

    total = lambda_intra * L_intra

    if gt_jersey is not None:
        # Jersey embedding classification (simple InfoNCE with jersey number as class)
        L_jersey = intra_team_contrastive_loss(reid_out["f_jersey"], gt_jersey, teams)
        total = total + lambda_jersey * L_jersey
        breakdown["L_jersey"] = L_jersey.item()

    breakdown["L_total"] = total.item()
    return total, breakdown

"""Module 3: Uncertainty Propagation.

Aggregates per-stage uncertainties (amodal, Re-ID, jersey, action) into a
tracklet-level score and provides uncertainty-weighted distance for offline
GTA-Link style tracklet linking.

Reference: 05_research_design.md §4.4
Key equations:
    s_tracklet = w_a (1 - u_a) + w_r (1 - u_r) + w_j (1 - u_j)
    d_uw = sum_k lambda_k * (1 - max(u_i,k, u_j,k)) * d_k
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class UncertaintyPropagation(nn.Module):
    """Learnable weighted fusion of per-stage uncertainties.

    Inputs:
        u_a: (B, M, T) amodal uncertainty
        u_r: (B, M, T) re-id uncertainty
        u_j: (B, M, T) jersey uncertainty (optional, pass None to skip)
    Outputs:
        u_tracklet: (B, M) scalar uncertainty per tracklet
        s_tracklet: (B, M) scalar confidence score per tracklet
    """

    def __init__(self, temperature: float = 1.0):
        super().__init__()
        # Learnable fusion weights, initialized to equal
        self.w_a = nn.Parameter(torch.tensor(1.0))
        self.w_r = nn.Parameter(torch.tensor(1.0))
        self.w_j = nn.Parameter(torch.tensor(1.0))
        self.temperature = temperature

    def forward(self, u_a: torch.Tensor,
                u_r: torch.Tensor | None = None,
                u_j: torch.Tensor | None = None) -> dict:
        # Reduce over time to per-tracklet scalars (mean for stability)
        u_a_mean = u_a.mean(dim=-1)

        weights = [F.softplus(self.w_a) / self.temperature]
        numers = [F.softplus(self.w_a) / self.temperature * (1.0 - u_a_mean)]

        if u_r is not None:
            u_r_mean = u_r.mean(dim=-1)
            weights.append(F.softplus(self.w_r) / self.temperature)
            numers.append(F.softplus(self.w_r) / self.temperature * (1.0 - u_r_mean))

        if u_j is not None:
            u_j_mean = u_j.mean(dim=-1)
            weights.append(F.softplus(self.w_j) / self.temperature)
            numers.append(F.softplus(self.w_j) / self.temperature * (1.0 - u_j_mean))

        total_w = torch.stack(weights).sum()
        total_num = torch.stack(numers).sum(dim=0)
        s_tracklet = total_num / (total_w + 1e-6)

        u_tracklet = 1.0 - s_tracklet

        return {"u_tracklet": u_tracklet, "s_tracklet": s_tracklet}


def uncertainty_weighted_distance(
    d_app: torch.Tensor,
    d_jersey: torch.Tensor,
    d_team: torch.Tensor,
    d_motion: torch.Tensor,
    u_i: dict[str, torch.Tensor],
    u_j: dict[str, torch.Tensor],
    lambdas: tuple[float, float, float, float] = (1.0, 1.0, 0.5, 0.5),
) -> torch.Tensor:
    """Uncertainty-weighted GTA-Link distance between tracklet i and tracklet j.

    d_uw = sum_k lambda_k * (1 - max(u_{i,k}, u_{j,k})) * d_k

    where k iterates over (appearance, jersey, team, motion) feature channels.
    When either tracklet has high uncertainty in a channel, that channel's
    contribution is down-weighted.

    Args:
        d_app, d_jersey, d_team, d_motion: (...,) pair-wise distances
        u_i, u_j: dicts with keys 'app', 'jersey', 'team', 'motion' -> tensors
        lambdas: static channel weights
    Returns:
        tensor of same shape as d_app with combined distance.
    """
    la, lj, lt, lm = lambdas
    w_app = 1.0 - torch.maximum(u_i.get("app", torch.zeros_like(d_app)),
                                u_j.get("app", torch.zeros_like(d_app)))
    w_jersey = 1.0 - torch.maximum(u_i.get("jersey", torch.zeros_like(d_jersey)),
                                   u_j.get("jersey", torch.zeros_like(d_jersey)))
    w_team = 1.0 - torch.maximum(u_i.get("team", torch.zeros_like(d_team)),
                                 u_j.get("team", torch.zeros_like(d_team)))
    w_motion = 1.0 - torch.maximum(u_i.get("motion", torch.zeros_like(d_motion)),
                                   u_j.get("motion", torch.zeros_like(d_motion)))

    d = (la * w_app * d_app
         + lj * w_jersey * d_jersey
         + lt * w_team * d_team
         + lm * w_motion * d_motion)
    # Normalize by effective weight sum to keep distance in comparable range
    norm = la * w_app + lj * w_jersey + lt * w_team + lm * w_motion + 1e-6
    return d / norm


def expected_calibration_error(
    predictions: torch.Tensor,
    targets: torch.Tensor,
    confidences: torch.Tensor,
    n_bins: int = 15,
) -> float:
    """Standard ECE (Expected Calibration Error) metric.

    Args:
        predictions: (N,) predicted class labels
        targets:     (N,) ground-truth class labels
        confidences: (N,) predicted confidences in [0,1]
        n_bins:      number of equal-width bins
    Returns:
        scalar ECE in [0,1] (lower is better).
    """
    predictions = predictions.cpu()
    targets = targets.cpu()
    confidences = confidences.cpu()

    bin_edges = torch.linspace(0, 1, n_bins + 1)
    ece = 0.0
    N = confidences.numel()
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        mask = (confidences > lo) & (confidences <= hi)
        if mask.sum() == 0:
            continue
        acc = (predictions[mask] == targets[mask]).float().mean().item()
        conf = confidences[mask].mean().item()
        ece += (mask.sum().item() / N) * abs(acc - conf)
    return ece

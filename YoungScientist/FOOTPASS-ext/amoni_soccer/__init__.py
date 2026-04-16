"""AmoUni-SoccerTrack: Amodal + Uniform-aware + Uncertainty Propagation extension for FOOTPASS.

Modules:
- amodal_head: Soccer-Amodal Head (visible/amodal/occlusion mask + uncertainty)
- uniform_aware_reid: Uniform-aware Re-ID (part + pose + jersey-region + intra-team CL)
- uncertainty_graph: Uncertainty propagation across amodal → Re-ID → jersey → tracklet
- extended_taad: FOOTPASS TAAD wrapper with continuous visibility mask + uncertainty
- footpass_loader: helper to import FOOTPASS-main modules without modifying upstream
"""

from .amodal_head import SoccerAmodalHead
from .uniform_aware_reid import UniformAwareReID, intra_team_contrastive_loss
from .uncertainty_graph import UncertaintyPropagation, uncertainty_weighted_distance
from .extended_taad import ExtendedTAAD

__all__ = [
    "SoccerAmodalHead",
    "UniformAwareReID",
    "intra_team_contrastive_loss",
    "UncertaintyPropagation",
    "uncertainty_weighted_distance",
    "ExtendedTAAD",
]

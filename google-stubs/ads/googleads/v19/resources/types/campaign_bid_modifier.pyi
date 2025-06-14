import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import criteria

__protobuf__: Incomplete

class CampaignBidModifier(proto.Message):
    resource_name: str
    campaign: str
    criterion_id: int
    bid_modifier: float
    interaction_type: criteria.InteractionTypeInfo

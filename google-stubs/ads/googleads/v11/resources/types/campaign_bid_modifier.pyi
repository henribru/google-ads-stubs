from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import InteractionTypeInfo

class CampaignBidModifier(proto.Message):
    resource_name: str
    campaign: str
    criterion_id: int
    bid_modifier: float
    interaction_type: InteractionTypeInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        criterion_id: int = ...,
        bid_modifier: float = ...,
        interaction_type: InteractionTypeInfo = ...
    ) -> None: ...

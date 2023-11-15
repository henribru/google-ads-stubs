from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.criteria import InteractionTypeInfo

_M = TypeVar("_M")

class CampaignBidModifier(proto.Message):
    resource_name: str
    campaign: str
    criterion_id: int
    bid_modifier: float
    interaction_type: InteractionTypeInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        criterion_id: int = ...,
        bid_modifier: float = ...,
        interaction_type: InteractionTypeInfo = ...
    ) -> None: ...

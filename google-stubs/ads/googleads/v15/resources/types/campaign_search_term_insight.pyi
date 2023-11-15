from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CampaignSearchTermInsight(proto.Message):
    resource_name: str
    category_label: str
    id: int
    campaign_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        category_label: str = ...,
        id: int = ...,
        campaign_id: int = ...
    ) -> None: ...

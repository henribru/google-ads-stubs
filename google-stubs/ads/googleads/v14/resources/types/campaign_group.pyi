from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.campaign_group_status import (
    CampaignGroupStatusEnum,
)

_M = TypeVar("_M")

class CampaignGroup(proto.Message):
    resource_name: str
    id: int
    name: str
    status: CampaignGroupStatusEnum.CampaignGroupStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: CampaignGroupStatusEnum.CampaignGroupStatus = ...
    ) -> None: ...

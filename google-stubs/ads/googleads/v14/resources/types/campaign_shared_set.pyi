from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.campaign_shared_set_status import (
    CampaignSharedSetStatusEnum,
)

_M = TypeVar("_M")

class CampaignSharedSet(proto.Message):
    resource_name: str
    campaign: str
    shared_set: str
    status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        shared_set: str = ...,
        status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus = ...
    ) -> None: ...

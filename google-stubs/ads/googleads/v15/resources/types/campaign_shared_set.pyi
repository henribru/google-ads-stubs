from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.campaign_shared_set_status import (
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
        status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "campaign", "shared_set", "status"]
    ) -> bool: ...

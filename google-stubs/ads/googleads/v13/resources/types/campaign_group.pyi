from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.campaign_group_status import (
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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: CampaignGroupStatusEnum.CampaignGroupStatus = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "name", "status"]) -> bool: ...  # type: ignore[override]

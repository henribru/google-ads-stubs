from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.asset_set_link_status import (
    AssetSetLinkStatusEnum,
)

_M = TypeVar("_M")

class CampaignAssetSet(proto.Message):
    resource_name: str
    campaign: str
    asset_set: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        asset_set: str = ...,
        status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "campaign", "asset_set", "status"]) -> bool: ...  # type: ignore[override]

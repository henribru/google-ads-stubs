from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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

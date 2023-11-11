from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.asset_set_link_status import (
    AssetSetLinkStatusEnum,
)

_M = TypeVar("_M")

class CustomerAssetSet(proto.Message):
    resource_name: str
    asset_set: str
    customer: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set: str = ...,
        customer: str = ...,
        status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...
    ) -> None: ...

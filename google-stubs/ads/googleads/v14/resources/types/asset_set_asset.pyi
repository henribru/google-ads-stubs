from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.asset_set_asset_status import (
    AssetSetAssetStatusEnum,
)

_M = TypeVar("_M")

class AssetSetAsset(proto.Message):
    resource_name: str
    asset_set: str
    asset: str
    status: AssetSetAssetStatusEnum.AssetSetAssetStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_set: str = ...,
        asset: str = ...,
        status: AssetSetAssetStatusEnum.AssetSetAssetStatus = ...
    ) -> None: ...

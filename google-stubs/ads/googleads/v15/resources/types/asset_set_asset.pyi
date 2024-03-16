from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.asset_set_asset_status import (
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
        status: AssetSetAssetStatusEnum.AssetSetAssetStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_set", "asset", "status"]
    ) -> bool: ...

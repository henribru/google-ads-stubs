from google.ads.googleads.v19.enums.types.asset_set_asset_status import AssetSetAssetStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetSetAsset(proto.Message):
    resource_name: str
    asset_set: str
    asset: str
    status: AssetSetAssetStatusEnum.AssetSetAssetStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., asset_set: str = ..., asset: str = ..., status: AssetSetAssetStatusEnum.AssetSetAssetStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "asset_set", "asset", "status"]) -> bool: ...

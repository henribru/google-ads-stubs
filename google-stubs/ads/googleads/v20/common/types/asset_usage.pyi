from google.ads.googleads.v20.enums.types.served_asset_field_type import ServedAssetFieldTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetUsage(proto.Message):
    asset: str
    served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., asset: str = ..., served_asset_field_type: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["asset", "served_asset_field_type"]) -> bool: ...

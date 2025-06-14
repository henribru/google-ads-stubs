from google.ads.googleads.v20.enums.types.asset_field_type import AssetFieldTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetFieldTypeView(proto.Message):
    resource_name: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "field_type"]) -> bool: ...

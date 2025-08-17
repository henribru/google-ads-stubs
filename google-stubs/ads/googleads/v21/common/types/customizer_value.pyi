from google.ads.googleads.v21.enums.types.customizer_attribute_type import CustomizerAttributeTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomizerValue(proto.Message):
    type_: CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, type_: CustomizerAttributeTypeEnum.CustomizerAttributeType = ..., string_value: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["type_", "string_value"]) -> bool: ...

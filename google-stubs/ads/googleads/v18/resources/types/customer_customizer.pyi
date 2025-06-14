from google.ads.googleads.v18.common.types.customizer_value import CustomizerValue
from google.ads.googleads.v18.enums.types.customizer_value_status import CustomizerValueStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerCustomizer(proto.Message):
    resource_name: str
    customizer_attribute: str
    status: CustomizerValueStatusEnum.CustomizerValueStatus
    value: CustomizerValue
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., customizer_attribute: str = ..., status: CustomizerValueStatusEnum.CustomizerValueStatus = ..., value: CustomizerValue = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "customizer_attribute", "status", "value"]) -> bool: ...

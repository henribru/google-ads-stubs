from google.ads.googleads.v22.enums.types.mobile_device_type import MobileDeviceTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MobileDeviceConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    manufacturer_name: str
    operating_system_name: str
    type_: MobileDeviceTypeEnum.MobileDeviceType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., name: str = ..., manufacturer_name: str = ..., operating_system_name: str = ..., type_: MobileDeviceTypeEnum.MobileDeviceType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "name", "manufacturer_name", "operating_system_name", "type_"]) -> bool: ...

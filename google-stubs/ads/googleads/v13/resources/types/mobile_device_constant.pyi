from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.mobile_device_type import MobileDeviceTypeEnum

_M = TypeVar("_M")

class MobileDeviceConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    manufacturer_name: str
    operating_system_name: str
    type_: MobileDeviceTypeEnum.MobileDeviceType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        manufacturer_name: str = ...,
        operating_system_name: str = ...,
        type_: MobileDeviceTypeEnum.MobileDeviceType = ...
    ) -> None: ...

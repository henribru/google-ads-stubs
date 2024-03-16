from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.mobile_device_type import MobileDeviceTypeEnum

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
        type_: MobileDeviceTypeEnum.MobileDeviceType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "manufacturer_name",
            "operating_system_name",
            "type_",
        ],
    ) -> bool: ...

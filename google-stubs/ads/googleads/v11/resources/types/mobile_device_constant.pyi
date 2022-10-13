from typing import Any

import proto

from google.ads.googleads.v11.enums.types.mobile_device_type import MobileDeviceTypeEnum

class MobileDeviceConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    manufacturer_name: str
    operating_system_name: str
    type_: MobileDeviceTypeEnum.MobileDeviceType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        manufacturer_name: str = ...,
        operating_system_name: str = ...,
        type_: MobileDeviceTypeEnum.MobileDeviceType = ...
    ) -> None: ...

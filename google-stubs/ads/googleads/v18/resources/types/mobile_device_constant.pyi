import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import mobile_device_type

__protobuf__: Incomplete

class MobileDeviceConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    manufacturer_name: str
    operating_system_name: str
    type_: mobile_device_type.MobileDeviceTypeEnum.MobileDeviceType

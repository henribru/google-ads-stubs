import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import customizer_attribute_status, customizer_attribute_type

__protobuf__: Incomplete

class CustomizerAttribute(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: customizer_attribute_type.CustomizerAttributeTypeEnum.CustomizerAttributeType
    status: customizer_attribute_status.CustomizerAttributeStatusEnum.CustomizerAttributeStatus

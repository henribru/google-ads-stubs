import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import customizer_attribute_type

__protobuf__: Incomplete

class CustomizerValue(proto.Message):
    type_: customizer_attribute_type.CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str

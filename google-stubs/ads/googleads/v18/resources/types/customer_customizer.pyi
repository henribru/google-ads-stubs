import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import customizer_value
from google.ads.googleads.v18.enums.types import customizer_value_status

__protobuf__: Incomplete

class CustomerCustomizer(proto.Message):
    resource_name: str
    customizer_attribute: str
    status: customizer_value_status.CustomizerValueStatusEnum.CustomizerValueStatus
    value: customizer_value.CustomizerValue

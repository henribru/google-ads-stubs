import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import customizer_value
from google.ads.googleads.v20.enums.types import customizer_value_status

__protobuf__: Incomplete

class AdGroupCustomizer(proto.Message):
    resource_name: str
    ad_group: str
    customizer_attribute: str
    status: customizer_value_status.CustomizerValueStatusEnum.CustomizerValueStatus
    value: customizer_value.CustomizerValue

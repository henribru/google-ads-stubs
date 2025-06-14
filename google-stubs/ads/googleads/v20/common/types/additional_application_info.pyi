import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import application_instance as gage_application_instance

__protobuf__: Incomplete

class AdditionalApplicationInfo(proto.Message):
    application_id: str
    application_instance: gage_application_instance.ApplicationInstanceEnum.ApplicationInstance

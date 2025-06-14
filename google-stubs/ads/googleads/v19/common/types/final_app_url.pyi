import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import app_url_operating_system_type

__protobuf__: Incomplete

class FinalAppUrl(proto.Message):
    os_type: app_url_operating_system_type.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    url: str

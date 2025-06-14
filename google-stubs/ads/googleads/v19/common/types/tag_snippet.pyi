import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import tracking_code_page_format, tracking_code_type

__protobuf__: Incomplete

class TagSnippet(proto.Message):
    type_: tracking_code_type.TrackingCodeTypeEnum.TrackingCodeType
    page_format: tracking_code_page_format.TrackingCodePageFormatEnum.TrackingCodePageFormat
    global_site_tag: str
    event_snippet: str

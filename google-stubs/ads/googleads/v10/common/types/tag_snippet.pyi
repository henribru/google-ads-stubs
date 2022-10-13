from typing import Any

import proto

from google.ads.googleads.v10.enums.types.tracking_code_page_format import (
    TrackingCodePageFormatEnum,
)
from google.ads.googleads.v10.enums.types.tracking_code_type import TrackingCodeTypeEnum

class TagSnippet(proto.Message):
    type_: TrackingCodeTypeEnum.TrackingCodeType
    page_format: TrackingCodePageFormatEnum.TrackingCodePageFormat
    global_site_tag: str
    event_snippet: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        type_: TrackingCodeTypeEnum.TrackingCodeType = ...,
        page_format: TrackingCodePageFormatEnum.TrackingCodePageFormat = ...,
        global_site_tag: str = ...,
        event_snippet: str = ...
    ) -> None: ...

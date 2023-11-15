from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.tracking_code_page_format import (
    TrackingCodePageFormatEnum,
)
from google.ads.googleads.v14.enums.types.tracking_code_type import TrackingCodeTypeEnum

_M = TypeVar("_M")

class TagSnippet(proto.Message):
    type_: TrackingCodeTypeEnum.TrackingCodeType
    page_format: TrackingCodePageFormatEnum.TrackingCodePageFormat
    global_site_tag: str
    event_snippet: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        type_: TrackingCodeTypeEnum.TrackingCodeType = ...,
        page_format: TrackingCodePageFormatEnum.TrackingCodePageFormat = ...,
        global_site_tag: str = ...,
        event_snippet: str = ...
    ) -> None: ...

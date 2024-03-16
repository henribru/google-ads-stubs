from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.tracking_code_page_format import (
    TrackingCodePageFormatEnum,
)
from google.ads.googleads.v15.enums.types.tracking_code_type import TrackingCodeTypeEnum

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
        event_snippet: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["type_", "page_format", "global_site_tag", "event_snippet"]
    ) -> bool: ...

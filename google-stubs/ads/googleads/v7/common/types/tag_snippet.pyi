from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    tracking_code_page_format as tracking_code_page_format,
    tracking_code_type as tracking_code_type,
)

__protobuf__: Any

class TagSnippet(proto.Message):
    type_: Any
    page_format: Any
    global_site_tag: Any
    event_snippet: Any

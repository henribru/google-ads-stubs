from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    search_term_targeting_status as search_term_targeting_status,
)

__protobuf__: Any

class SearchTermView(proto.Message):
    resource_name: Any
    search_term: Any
    ad_group: Any
    status: Any

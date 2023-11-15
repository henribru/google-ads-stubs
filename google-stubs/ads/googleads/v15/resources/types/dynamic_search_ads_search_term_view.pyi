from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class DynamicSearchAdsSearchTermView(proto.Message):
    resource_name: str
    search_term: str
    headline: str
    landing_page: str
    page_url: str
    has_negative_keyword: bool
    has_matching_keyword: bool
    has_negative_url: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        search_term: str = ...,
        headline: str = ...,
        landing_page: str = ...,
        page_url: str = ...,
        has_negative_keyword: bool = ...,
        has_matching_keyword: bool = ...,
        has_negative_url: bool = ...
    ) -> None: ...

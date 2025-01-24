from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        has_negative_url: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "search_term",
            "headline",
            "landing_page",
            "page_url",
            "has_negative_keyword",
            "has_matching_keyword",
            "has_negative_url",
        ],
    ) -> bool: ...

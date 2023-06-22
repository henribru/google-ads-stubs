from typing import Any

import proto

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        search_term: str = ...,
        headline: str = ...,
        landing_page: str = ...,
        page_url: str = ...,
        has_negative_keyword: bool = ...,
        has_matching_keyword: bool = ...,
        has_negative_url: bool = ...
    ) -> None: ...

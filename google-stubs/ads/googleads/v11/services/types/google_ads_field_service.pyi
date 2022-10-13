from typing import Any

import proto

from google.ads.googleads.v11.resources.types.google_ads_field import GoogleAdsField

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: str
    page_token: str
    page_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        query: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...

class SearchGoogleAdsFieldsResponse(proto.Message):
    results: list[GoogleAdsField]
    next_page_token: str
    total_results_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[GoogleAdsField] = ...,
        next_page_token: str = ...,
        total_results_count: int = ...
    ) -> None: ...

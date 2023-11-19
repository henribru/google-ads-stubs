from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.resources.types.google_ads_field import GoogleAdsField

_M = TypeVar("_M")

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: str
    page_token: str
    page_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        query: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["query", "page_token", "page_size"]) -> bool: ...  # type: ignore[override]

class SearchGoogleAdsFieldsResponse(proto.Message):
    results: MutableSequence[GoogleAdsField]
    next_page_token: str
    total_results_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[GoogleAdsField] = ...,
        next_page_token: str = ...,
        total_results_count: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results", "next_page_token", "total_results_count"]) -> bool: ...  # type: ignore[override]

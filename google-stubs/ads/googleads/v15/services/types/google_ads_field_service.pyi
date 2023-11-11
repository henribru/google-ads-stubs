from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.resources.types.google_ads_field import GoogleAdsField

_M = TypeVar("_M")

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: str
    page_token: str
    page_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        query: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...

class SearchGoogleAdsFieldsResponse(proto.Message):
    results: MutableSequence[GoogleAdsField]
    next_page_token: str
    total_results_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[GoogleAdsField] = ...,
        next_page_token: str = ...,
        total_results_count: int = ...
    ) -> None: ...

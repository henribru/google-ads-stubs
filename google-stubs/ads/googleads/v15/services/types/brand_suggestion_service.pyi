from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.brand_state import BrandStateEnum

_M = TypeVar("_M")

class BrandSuggestion(proto.Message):
    id: str
    name: str
    urls: MutableSequence[str]
    state: BrandStateEnum.BrandState
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        id: str = ...,
        name: str = ...,
        urls: MutableSequence[str] = ...,
        state: BrandStateEnum.BrandState = ...
    ) -> None: ...

class SuggestBrandsRequest(proto.Message):
    customer_id: str
    brand_prefix: str
    selected_brands: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        brand_prefix: str = ...,
        selected_brands: MutableSequence[str] = ...
    ) -> None: ...

class SuggestBrandsResponse(proto.Message):
    brands: MutableSequence[BrandSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        brands: MutableSequence[BrandSuggestion] = ...
    ) -> None: ...

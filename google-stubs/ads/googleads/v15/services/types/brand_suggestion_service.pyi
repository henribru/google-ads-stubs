from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.brand_state import BrandStateEnum

_M = TypeVar("_M")

class BrandSuggestion(proto.Message):
    id: str
    name: str
    urls: MutableSequence[str]
    state: BrandStateEnum.BrandState
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: str = ...,
        name: str = ...,
        urls: MutableSequence[str] = ...,
        state: BrandStateEnum.BrandState = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["id", "name", "urls", "state"]
    ) -> bool: ...

class SuggestBrandsRequest(proto.Message):
    customer_id: str
    brand_prefix: str
    selected_brands: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        brand_prefix: str = ...,
        selected_brands: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "brand_prefix", "selected_brands"]
    ) -> bool: ...

class SuggestBrandsResponse(proto.Message):
    brands: MutableSequence[BrandSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        brands: MutableSequence[BrandSuggestion] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["brands"]
    ) -> bool: ...

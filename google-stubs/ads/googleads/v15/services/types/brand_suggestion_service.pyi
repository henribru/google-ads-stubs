from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.enums.types.brand_state import BrandStateEnum

class BrandSuggestion(proto.Message):
    id: str
    name: str
    urls: MutableSequence[str]
    state: BrandStateEnum.BrandState
    def __init__(
        self,
        mapping: Any | None = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        brand_prefix: str = ...,
        selected_brands: MutableSequence[str] = ...
    ) -> None: ...

class SuggestBrandsResponse(proto.Message):
    brands: MutableSequence[BrandSuggestion]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        brands: MutableSequence[BrandSuggestion] = ...
    ) -> None: ...

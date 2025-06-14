from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.brand_state import BrandStateEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BrandSuggestion(proto.Message):
    id: str
    name: str
    urls: MutableSequence[str]
    state: BrandStateEnum.BrandState
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., id: str = ..., name: str = ..., urls: MutableSequence[str] = ..., state: BrandStateEnum.BrandState = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["id", "name", "urls", "state"]) -> bool: ...
class SuggestBrandsRequest(proto.Message):
    customer_id: str
    brand_prefix: str
    selected_brands: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., brand_prefix: str = ..., selected_brands: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "brand_prefix", "selected_brands"]) -> bool: ...
class SuggestBrandsResponse(proto.Message):
    brands: MutableSequence[BrandSuggestion]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., brands: MutableSequence[BrandSuggestion] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["brands"]) -> bool: ...

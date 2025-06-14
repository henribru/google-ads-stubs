from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.feed_item_set_string_filter_type import FeedItemSetStringFilterTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BusinessNameFilter(proto.Message):
    business_name: str
    filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, business_name: str = ..., filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["business_name", "filter_type"]) -> bool: ...
class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: MutableSequence[int]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, chain_ids: MutableSequence[int] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["chain_ids"]) -> bool: ...
class DynamicLocationSetFilter(proto.Message):
    labels: MutableSequence[str]
    business_name_filter: BusinessNameFilter
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, labels: MutableSequence[str] = ..., business_name_filter: BusinessNameFilter = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["labels", "business_name_filter"]) -> bool: ...

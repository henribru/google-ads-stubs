from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.feed_item_set_string_filter_type import (
    FeedItemSetStringFilterTypeEnum,
)

_M = TypeVar("_M")

class BusinessNameFilter(proto.Message):
    business_name: str
    filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name: str = ...,
        filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["business_name", "filter_type"]) -> bool: ...  # type: ignore[override]

class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: MutableSequence[int]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        chain_ids: MutableSequence[int] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["chain_ids"]) -> bool: ...  # type: ignore[override]

class DynamicLocationSetFilter(proto.Message):
    labels: MutableSequence[str]
    business_name_filter: BusinessNameFilter
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        labels: MutableSequence[str] = ...,
        business_name_filter: BusinessNameFilter = ...
    ) -> None: ...
    def __contains__(self, key: Literal["labels", "business_name_filter"]) -> bool: ...  # type: ignore[override]

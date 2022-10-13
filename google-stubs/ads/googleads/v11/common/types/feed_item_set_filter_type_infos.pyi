from typing import Any

import proto

from google.ads.googleads.v11.enums.types.feed_item_set_string_filter_type import (
    FeedItemSetStringFilterTypeEnum,
)

class BusinessNameFilter(proto.Message):
    business_name: str
    filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        filter_type: FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType = ...
    ) -> None: ...

class DynamicAffiliateLocationSetFilter(proto.Message):
    chain_ids: list[int]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        chain_ids: list[int] = ...
    ) -> None: ...

class DynamicLocationSetFilter(proto.Message):
    labels: list[str]
    business_name_filter: BusinessNameFilter
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        labels: list[str] = ...,
        business_name_filter: BusinessNameFilter = ...
    ) -> None: ...

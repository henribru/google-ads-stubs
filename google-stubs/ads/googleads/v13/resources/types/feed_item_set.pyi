from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.feed_item_set_filter_type_infos import (
    DynamicAffiliateLocationSetFilter,
    DynamicLocationSetFilter,
)
from google.ads.googleads.v13.enums.types.feed_item_set_status import (
    FeedItemSetStatusEnum,
)

_M = TypeVar("_M")

class FeedItemSet(proto.Message):
    resource_name: str
    feed: str
    feed_item_set_id: int
    display_name: str
    status: FeedItemSetStatusEnum.FeedItemSetStatus
    dynamic_location_set_filter: DynamicLocationSetFilter
    dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed: str = ...,
        feed_item_set_id: int = ...,
        display_name: str = ...,
        status: FeedItemSetStatusEnum.FeedItemSetStatus = ...,
        dynamic_location_set_filter: DynamicLocationSetFilter = ...,
        dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter = ...
    ) -> None: ...

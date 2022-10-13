from typing import Any

import proto

from google.ads.googleads.v10.common.types.feed_item_set_filter_type_infos import (
    DynamicAffiliateLocationSetFilter,
    DynamicLocationSetFilter,
)
from google.ads.googleads.v10.enums.types.feed_item_set_status import (
    FeedItemSetStatusEnum,
)

class FeedItemSet(proto.Message):
    resource_name: str
    feed: str
    feed_item_set_id: int
    display_name: str
    status: FeedItemSetStatusEnum.FeedItemSetStatus
    dynamic_location_set_filter: DynamicLocationSetFilter
    dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter
    def __init__(
        self,
        mapping: Any | None = ...,
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

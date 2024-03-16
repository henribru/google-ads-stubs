from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.feed_item_set_filter_type_infos import (
    DynamicAffiliateLocationSetFilter,
    DynamicLocationSetFilter,
)
from google.ads.googleads.v14.enums.types.feed_item_set_status import (
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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        feed: str = ...,
        feed_item_set_id: int = ...,
        display_name: str = ...,
        status: FeedItemSetStatusEnum.FeedItemSetStatus = ...,
        dynamic_location_set_filter: DynamicLocationSetFilter = ...,
        dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "feed",
            "feed_item_set_id",
            "display_name",
            "status",
            "dynamic_location_set_filter",
            "dynamic_affiliate_location_set_filter",
        ],
    ) -> bool: ...

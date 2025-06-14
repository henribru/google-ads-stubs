from google.ads.googleads.v18.common.types.feed_item_set_filter_type_infos import DynamicAffiliateLocationSetFilter
from google.ads.googleads.v18.common.types.feed_item_set_filter_type_infos import DynamicLocationSetFilter
from google.ads.googleads.v18.enums.types.feed_item_set_status import FeedItemSetStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedItemSet(proto.Message):
    resource_name: str
    feed: str
    feed_item_set_id: int
    display_name: str
    status: FeedItemSetStatusEnum.FeedItemSetStatus
    dynamic_location_set_filter: DynamicLocationSetFilter
    dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., feed: str = ..., feed_item_set_id: int = ..., display_name: str = ..., status: FeedItemSetStatusEnum.FeedItemSetStatus = ..., dynamic_location_set_filter: DynamicLocationSetFilter = ..., dynamic_affiliate_location_set_filter: DynamicAffiliateLocationSetFilter = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "feed", "feed_item_set_id", "display_name", "status", "dynamic_location_set_filter", "dynamic_affiliate_location_set_filter"]) -> bool: ...

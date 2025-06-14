import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import feed_item_set_filter_type_infos
from google.ads.googleads.v18.enums.types import feed_item_set_status

__protobuf__: Incomplete

class FeedItemSet(proto.Message):
    resource_name: str
    feed: str
    feed_item_set_id: int
    display_name: str
    status: feed_item_set_status.FeedItemSetStatusEnum.FeedItemSetStatus
    dynamic_location_set_filter: feed_item_set_filter_type_infos.DynamicLocationSetFilter
    dynamic_affiliate_location_set_filter: feed_item_set_filter_type_infos.DynamicAffiliateLocationSetFilter

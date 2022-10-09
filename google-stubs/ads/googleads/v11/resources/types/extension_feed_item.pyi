import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    criteria as criteria,
    extensions as extensions,
)
from google.ads.googleads.v11.enums.types import (
    feed_item_status as feed_item_status,
    feed_item_target_device as feed_item_target_device,
)

__protobuf__: Incomplete

class ExtensionFeedItem(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    extension_type: Incomplete
    start_date_time: Incomplete
    end_date_time: Incomplete
    ad_schedules: Incomplete
    device: Incomplete
    targeted_geo_target_constant: Incomplete
    targeted_keyword: Incomplete
    status: Incomplete
    sitelink_feed_item: Incomplete
    structured_snippet_feed_item: Incomplete
    app_feed_item: Incomplete
    call_feed_item: Incomplete
    callout_feed_item: Incomplete
    text_message_feed_item: Incomplete
    price_feed_item: Incomplete
    promotion_feed_item: Incomplete
    location_feed_item: Incomplete
    affiliate_location_feed_item: Incomplete
    hotel_callout_feed_item: Incomplete
    image_feed_item: Incomplete
    targeted_campaign: Incomplete
    targeted_ad_group: Incomplete

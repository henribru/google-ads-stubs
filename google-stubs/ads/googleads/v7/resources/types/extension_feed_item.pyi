from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    criteria as criteria,
    extensions as extensions,
)
from google.ads.googleads.v7.enums.types import (
    feed_item_status as feed_item_status,
    feed_item_target_device as feed_item_target_device,
)

__protobuf__: Any

class ExtensionFeedItem(proto.Message):
    resource_name: Any
    id: Any
    extension_type: Any
    start_date_time: Any
    end_date_time: Any
    ad_schedules: Any
    device: Any
    targeted_geo_target_constant: Any
    targeted_keyword: Any
    status: Any
    sitelink_feed_item: Any
    structured_snippet_feed_item: Any
    app_feed_item: Any
    call_feed_item: Any
    callout_feed_item: Any
    text_message_feed_item: Any
    price_feed_item: Any
    promotion_feed_item: Any
    location_feed_item: Any
    affiliate_location_feed_item: Any
    hotel_callout_feed_item: Any
    image_feed_item: Any
    targeted_campaign: Any
    targeted_ad_group: Any

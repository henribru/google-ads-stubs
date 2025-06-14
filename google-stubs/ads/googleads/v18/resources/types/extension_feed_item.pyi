import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria, extensions
from google.ads.googleads.v18.enums.types import extension_type as gage_extension_type, feed_item_status, feed_item_target_device
from typing import MutableSequence

__protobuf__: Incomplete

class ExtensionFeedItem(proto.Message):
    resource_name: str
    id: int
    extension_type: gage_extension_type.ExtensionTypeEnum.ExtensionType
    start_date_time: str
    end_date_time: str
    ad_schedules: MutableSequence[criteria.AdScheduleInfo]
    device: feed_item_target_device.FeedItemTargetDeviceEnum.FeedItemTargetDevice
    targeted_geo_target_constant: str
    targeted_keyword: criteria.KeywordInfo
    status: feed_item_status.FeedItemStatusEnum.FeedItemStatus
    sitelink_feed_item: extensions.SitelinkFeedItem
    structured_snippet_feed_item: extensions.StructuredSnippetFeedItem
    app_feed_item: extensions.AppFeedItem
    call_feed_item: extensions.CallFeedItem
    callout_feed_item: extensions.CalloutFeedItem
    text_message_feed_item: extensions.TextMessageFeedItem
    price_feed_item: extensions.PriceFeedItem
    promotion_feed_item: extensions.PromotionFeedItem
    location_feed_item: extensions.LocationFeedItem
    affiliate_location_feed_item: extensions.AffiliateLocationFeedItem
    hotel_callout_feed_item: extensions.HotelCalloutFeedItem
    image_feed_item: extensions.ImageFeedItem
    targeted_campaign: str
    targeted_ad_group: str

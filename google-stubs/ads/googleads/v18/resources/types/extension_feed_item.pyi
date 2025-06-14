from google.ads.googleads.v18.common.types.extensions import ImageFeedItem
from google.ads.googleads.v18.common.types.extensions import HotelCalloutFeedItem
from google.ads.googleads.v18.common.types.extensions import AffiliateLocationFeedItem
from google.ads.googleads.v18.common.types.extensions import LocationFeedItem
from google.ads.googleads.v18.common.types.extensions import PromotionFeedItem
from google.ads.googleads.v18.common.types.extensions import PriceFeedItem
from google.ads.googleads.v18.common.types.extensions import TextMessageFeedItem
from google.ads.googleads.v18.common.types.extensions import CalloutFeedItem
from google.ads.googleads.v18.common.types.extensions import CallFeedItem
from google.ads.googleads.v18.common.types.extensions import AppFeedItem
from google.ads.googleads.v18.common.types.extensions import StructuredSnippetFeedItem
from google.ads.googleads.v18.common.types.extensions import SitelinkFeedItem
from google.ads.googleads.v18.enums.types.feed_item_status import FeedItemStatusEnum
from google.ads.googleads.v18.common.types.criteria import KeywordInfo
from google.ads.googleads.v18.enums.types.feed_item_target_device import FeedItemTargetDeviceEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.criteria import AdScheduleInfo
from google.ads.googleads.v18.enums.types.extension_type import ExtensionTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ExtensionFeedItem(proto.Message):
    resource_name: str
    id: int
    extension_type: ExtensionTypeEnum.ExtensionType
    start_date_time: str
    end_date_time: str
    ad_schedules: MutableSequence[AdScheduleInfo]
    device: FeedItemTargetDeviceEnum.FeedItemTargetDevice
    targeted_geo_target_constant: str
    targeted_keyword: KeywordInfo
    status: FeedItemStatusEnum.FeedItemStatus
    sitelink_feed_item: SitelinkFeedItem
    structured_snippet_feed_item: StructuredSnippetFeedItem
    app_feed_item: AppFeedItem
    call_feed_item: CallFeedItem
    callout_feed_item: CalloutFeedItem
    text_message_feed_item: TextMessageFeedItem
    price_feed_item: PriceFeedItem
    promotion_feed_item: PromotionFeedItem
    location_feed_item: LocationFeedItem
    affiliate_location_feed_item: AffiliateLocationFeedItem
    hotel_callout_feed_item: HotelCalloutFeedItem
    image_feed_item: ImageFeedItem
    targeted_campaign: str
    targeted_ad_group: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., extension_type: ExtensionTypeEnum.ExtensionType = ..., start_date_time: str = ..., end_date_time: str = ..., ad_schedules: MutableSequence[AdScheduleInfo] = ..., device: FeedItemTargetDeviceEnum.FeedItemTargetDevice = ..., targeted_geo_target_constant: str = ..., targeted_keyword: KeywordInfo = ..., status: FeedItemStatusEnum.FeedItemStatus = ..., sitelink_feed_item: SitelinkFeedItem = ..., structured_snippet_feed_item: StructuredSnippetFeedItem = ..., app_feed_item: AppFeedItem = ..., call_feed_item: CallFeedItem = ..., callout_feed_item: CalloutFeedItem = ..., text_message_feed_item: TextMessageFeedItem = ..., price_feed_item: PriceFeedItem = ..., promotion_feed_item: PromotionFeedItem = ..., location_feed_item: LocationFeedItem = ..., affiliate_location_feed_item: AffiliateLocationFeedItem = ..., hotel_callout_feed_item: HotelCalloutFeedItem = ..., image_feed_item: ImageFeedItem = ..., targeted_campaign: str = ..., targeted_ad_group: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "extension_type", "start_date_time", "end_date_time", "ad_schedules", "device", "targeted_geo_target_constant", "targeted_keyword", "status", "sitelink_feed_item", "structured_snippet_feed_item", "app_feed_item", "call_feed_item", "callout_feed_item", "text_message_feed_item", "price_feed_item", "promotion_feed_item", "location_feed_item", "affiliate_location_feed_item", "hotel_callout_feed_item", "image_feed_item", "targeted_campaign", "targeted_ad_group"]) -> bool: ...

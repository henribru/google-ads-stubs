from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.criteria import AdScheduleInfo, KeywordInfo
from google.ads.googleads.v13.common.types.extensions import (
    AffiliateLocationFeedItem,
    AppFeedItem,
    CallFeedItem,
    CalloutFeedItem,
    HotelCalloutFeedItem,
    ImageFeedItem,
    LocationFeedItem,
    PriceFeedItem,
    PromotionFeedItem,
    SitelinkFeedItem,
    StructuredSnippetFeedItem,
    TextMessageFeedItem,
)
from google.ads.googleads.v13.enums.types.extension_type import ExtensionTypeEnum
from google.ads.googleads.v13.enums.types.feed_item_status import FeedItemStatusEnum
from google.ads.googleads.v13.enums.types.feed_item_target_device import (
    FeedItemTargetDeviceEnum,
)

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        extension_type: ExtensionTypeEnum.ExtensionType = ...,
        start_date_time: str = ...,
        end_date_time: str = ...,
        ad_schedules: MutableSequence[AdScheduleInfo] = ...,
        device: FeedItemTargetDeviceEnum.FeedItemTargetDevice = ...,
        targeted_geo_target_constant: str = ...,
        targeted_keyword: KeywordInfo = ...,
        status: FeedItemStatusEnum.FeedItemStatus = ...,
        sitelink_feed_item: SitelinkFeedItem = ...,
        structured_snippet_feed_item: StructuredSnippetFeedItem = ...,
        app_feed_item: AppFeedItem = ...,
        call_feed_item: CallFeedItem = ...,
        callout_feed_item: CalloutFeedItem = ...,
        text_message_feed_item: TextMessageFeedItem = ...,
        price_feed_item: PriceFeedItem = ...,
        promotion_feed_item: PromotionFeedItem = ...,
        location_feed_item: LocationFeedItem = ...,
        affiliate_location_feed_item: AffiliateLocationFeedItem = ...,
        hotel_callout_feed_item: HotelCalloutFeedItem = ...,
        image_feed_item: ImageFeedItem = ...,
        targeted_campaign: str = ...,
        targeted_ad_group: str = ...
    ) -> None: ...

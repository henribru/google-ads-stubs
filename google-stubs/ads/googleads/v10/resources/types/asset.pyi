from typing import Any

import proto

from google.ads.googleads.v10.common.types.asset_types import (
    BookOnGoogleAsset,
    CallAsset,
    CalloutAsset,
    CallToActionAsset,
    DiscoveryCarouselCardAsset,
    DynamicCustomAsset,
    DynamicEducationAsset,
    DynamicFlightsAsset,
    DynamicHotelsAndRentalsAsset,
    DynamicJobsAsset,
    DynamicLocalAsset,
    DynamicRealEstateAsset,
    DynamicTravelAsset,
    HotelCalloutAsset,
    ImageAsset,
    LeadFormAsset,
    MediaBundleAsset,
    MobileAppAsset,
    PageFeedAsset,
    PriceAsset,
    PromotionAsset,
    SitelinkAsset,
    StructuredSnippetAsset,
    TextAsset,
    YoutubeVideoAsset,
)
from google.ads.googleads.v10.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v10.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v10.enums.types.asset_type import AssetTypeEnum
from google.ads.googleads.v10.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v10.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

class Asset(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: AssetTypeEnum.AssetType
    final_urls: list[str]
    final_mobile_urls: list[str]
    tracking_url_template: str
    url_custom_parameters: list[CustomParameter]
    final_url_suffix: str
    policy_summary: AssetPolicySummary
    youtube_video_asset: YoutubeVideoAsset
    media_bundle_asset: MediaBundleAsset
    image_asset: ImageAsset
    text_asset: TextAsset
    lead_form_asset: LeadFormAsset
    book_on_google_asset: BookOnGoogleAsset
    promotion_asset: PromotionAsset
    callout_asset: CalloutAsset
    structured_snippet_asset: StructuredSnippetAsset
    sitelink_asset: SitelinkAsset
    page_feed_asset: PageFeedAsset
    dynamic_education_asset: DynamicEducationAsset
    mobile_app_asset: MobileAppAsset
    hotel_callout_asset: HotelCalloutAsset
    call_asset: CallAsset
    price_asset: PriceAsset
    call_to_action_asset: CallToActionAsset
    dynamic_real_estate_asset: DynamicRealEstateAsset
    dynamic_custom_asset: DynamicCustomAsset
    dynamic_hotels_and_rentals_asset: DynamicHotelsAndRentalsAsset
    dynamic_flights_asset: DynamicFlightsAsset
    discovery_carousel_card_asset: DiscoveryCarouselCardAsset
    dynamic_travel_asset: DynamicTravelAsset
    dynamic_local_asset: DynamicLocalAsset
    dynamic_jobs_asset: DynamicJobsAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: AssetTypeEnum.AssetType = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: list[CustomParameter] = ...,
        final_url_suffix: str = ...,
        policy_summary: AssetPolicySummary = ...,
        youtube_video_asset: YoutubeVideoAsset = ...,
        media_bundle_asset: MediaBundleAsset = ...,
        image_asset: ImageAsset = ...,
        text_asset: TextAsset = ...,
        lead_form_asset: LeadFormAsset = ...,
        book_on_google_asset: BookOnGoogleAsset = ...,
        promotion_asset: PromotionAsset = ...,
        callout_asset: CalloutAsset = ...,
        structured_snippet_asset: StructuredSnippetAsset = ...,
        sitelink_asset: SitelinkAsset = ...,
        page_feed_asset: PageFeedAsset = ...,
        dynamic_education_asset: DynamicEducationAsset = ...,
        mobile_app_asset: MobileAppAsset = ...,
        hotel_callout_asset: HotelCalloutAsset = ...,
        call_asset: CallAsset = ...,
        price_asset: PriceAsset = ...,
        call_to_action_asset: CallToActionAsset = ...,
        dynamic_real_estate_asset: DynamicRealEstateAsset = ...,
        dynamic_custom_asset: DynamicCustomAsset = ...,
        dynamic_hotels_and_rentals_asset: DynamicHotelsAndRentalsAsset = ...,
        dynamic_flights_asset: DynamicFlightsAsset = ...,
        discovery_carousel_card_asset: DiscoveryCarouselCardAsset = ...,
        dynamic_travel_asset: DynamicTravelAsset = ...,
        dynamic_local_asset: DynamicLocalAsset = ...,
        dynamic_jobs_asset: DynamicJobsAsset = ...
    ) -> None: ...

class AssetPolicySummary(proto.Message):
    policy_topic_entries: list[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: list[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...
    ) -> None: ...

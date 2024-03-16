from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.asset_types import (
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
    HotelPropertyAsset,
    ImageAsset,
    LeadFormAsset,
    LocationAsset,
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
from google.ads.googleads.v15.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v15.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v15.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v15.enums.types.asset_source import AssetSourceEnum
from google.ads.googleads.v15.enums.types.asset_type import AssetTypeEnum
from google.ads.googleads.v15.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v15.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

_M = TypeVar("_M")

class Asset(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: AssetTypeEnum.AssetType
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    final_url_suffix: str
    source: AssetSourceEnum.AssetSource
    policy_summary: AssetPolicySummary
    field_type_policy_summaries: MutableSequence[AssetFieldTypePolicySummary]
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
    location_asset: LocationAsset
    hotel_property_asset: HotelPropertyAsset
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        type_: AssetTypeEnum.AssetType = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        final_url_suffix: str = ...,
        source: AssetSourceEnum.AssetSource = ...,
        policy_summary: AssetPolicySummary = ...,
        field_type_policy_summaries: MutableSequence[AssetFieldTypePolicySummary] = ...,
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
        dynamic_jobs_asset: DynamicJobsAsset = ...,
        location_asset: LocationAsset = ...,
        hotel_property_asset: HotelPropertyAsset = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "type_",
            "final_urls",
            "final_mobile_urls",
            "tracking_url_template",
            "url_custom_parameters",
            "final_url_suffix",
            "source",
            "policy_summary",
            "field_type_policy_summaries",
            "youtube_video_asset",
            "media_bundle_asset",
            "image_asset",
            "text_asset",
            "lead_form_asset",
            "book_on_google_asset",
            "promotion_asset",
            "callout_asset",
            "structured_snippet_asset",
            "sitelink_asset",
            "page_feed_asset",
            "dynamic_education_asset",
            "mobile_app_asset",
            "hotel_callout_asset",
            "call_asset",
            "price_asset",
            "call_to_action_asset",
            "dynamic_real_estate_asset",
            "dynamic_custom_asset",
            "dynamic_hotels_and_rentals_asset",
            "dynamic_flights_asset",
            "discovery_carousel_card_asset",
            "dynamic_travel_asset",
            "dynamic_local_asset",
            "dynamic_jobs_asset",
            "location_asset",
            "hotel_property_asset",
        ],
    ) -> bool: ...

class AssetFieldTypePolicySummary(proto.Message):
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    asset_source: AssetSourceEnum.AssetSource
    policy_summary_info: AssetPolicySummary
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        asset_source: AssetSourceEnum.AssetSource = ...,
        policy_summary_info: AssetPolicySummary = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset_field_type", "asset_source", "policy_summary_info"]
    ) -> bool: ...

class AssetPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["policy_topic_entries", "review_status", "approval_status"]
    ) -> bool: ...

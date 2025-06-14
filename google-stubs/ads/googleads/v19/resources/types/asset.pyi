import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import asset_types, custom_parameter, policy
from google.ads.googleads.v19.enums.types import asset_field_type as gage_asset_field_type, asset_source as gage_asset_source, asset_type, policy_approval_status, policy_review_status
from typing import MutableSequence

__protobuf__: Incomplete

class Asset(proto.Message):
    resource_name: str
    id: int
    name: str
    type_: asset_type.AssetTypeEnum.AssetType
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    final_url_suffix: str
    source: gage_asset_source.AssetSourceEnum.AssetSource
    policy_summary: AssetPolicySummary
    field_type_policy_summaries: MutableSequence['AssetFieldTypePolicySummary']
    youtube_video_asset: asset_types.YoutubeVideoAsset
    media_bundle_asset: asset_types.MediaBundleAsset
    image_asset: asset_types.ImageAsset
    text_asset: asset_types.TextAsset
    lead_form_asset: asset_types.LeadFormAsset
    book_on_google_asset: asset_types.BookOnGoogleAsset
    promotion_asset: asset_types.PromotionAsset
    callout_asset: asset_types.CalloutAsset
    structured_snippet_asset: asset_types.StructuredSnippetAsset
    sitelink_asset: asset_types.SitelinkAsset
    page_feed_asset: asset_types.PageFeedAsset
    dynamic_education_asset: asset_types.DynamicEducationAsset
    mobile_app_asset: asset_types.MobileAppAsset
    hotel_callout_asset: asset_types.HotelCalloutAsset
    call_asset: asset_types.CallAsset
    price_asset: asset_types.PriceAsset
    call_to_action_asset: asset_types.CallToActionAsset
    dynamic_real_estate_asset: asset_types.DynamicRealEstateAsset
    dynamic_custom_asset: asset_types.DynamicCustomAsset
    dynamic_hotels_and_rentals_asset: asset_types.DynamicHotelsAndRentalsAsset
    dynamic_flights_asset: asset_types.DynamicFlightsAsset
    demand_gen_carousel_card_asset: asset_types.DemandGenCarouselCardAsset
    dynamic_travel_asset: asset_types.DynamicTravelAsset
    dynamic_local_asset: asset_types.DynamicLocalAsset
    dynamic_jobs_asset: asset_types.DynamicJobsAsset
    location_asset: asset_types.LocationAsset
    hotel_property_asset: asset_types.HotelPropertyAsset
    business_message_asset: asset_types.BusinessMessageAsset
    app_deep_link_asset: asset_types.AppDeepLinkAsset

class AssetFieldTypePolicySummary(proto.Message):
    asset_field_type: gage_asset_field_type.AssetFieldTypeEnum.AssetFieldType
    asset_source: gage_asset_source.AssetSourceEnum.AssetSource
    policy_summary_info: AssetPolicySummary

class AssetPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus

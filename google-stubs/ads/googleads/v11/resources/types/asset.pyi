import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    asset_types as asset_types,
    custom_parameter as custom_parameter,
    policy as policy,
)
from google.ads.googleads.v11.enums.types import (
    asset_source as asset_source,
    asset_type as asset_type,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Incomplete

class Asset(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    type_: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    final_url_suffix: Incomplete
    source: Incomplete
    policy_summary: Incomplete
    youtube_video_asset: Incomplete
    media_bundle_asset: Incomplete
    image_asset: Incomplete
    text_asset: Incomplete
    lead_form_asset: Incomplete
    book_on_google_asset: Incomplete
    promotion_asset: Incomplete
    callout_asset: Incomplete
    structured_snippet_asset: Incomplete
    sitelink_asset: Incomplete
    page_feed_asset: Incomplete
    dynamic_education_asset: Incomplete
    mobile_app_asset: Incomplete
    hotel_callout_asset: Incomplete
    call_asset: Incomplete
    price_asset: Incomplete
    call_to_action_asset: Incomplete
    dynamic_real_estate_asset: Incomplete
    dynamic_custom_asset: Incomplete
    dynamic_hotels_and_rentals_asset: Incomplete
    dynamic_flights_asset: Incomplete
    discovery_carousel_card_asset: Incomplete
    dynamic_travel_asset: Incomplete
    dynamic_local_asset: Incomplete
    dynamic_jobs_asset: Incomplete

class AssetPolicySummary(proto.Message):
    policy_topic_entries: Incomplete
    review_status: Incomplete
    approval_status: Incomplete

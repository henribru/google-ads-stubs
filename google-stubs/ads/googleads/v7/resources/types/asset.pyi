from typing import Any

import proto

from google.ads.googleads.v7.common.types import (
    asset_types as asset_types,
    custom_parameter as custom_parameter,
)
from google.ads.googleads.v7.enums.types import (
    asset_type as asset_type,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Any

class Asset(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    type_: Any
    final_urls: Any
    final_mobile_urls: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    final_url_suffix: Any
    policy_summary: Any
    youtube_video_asset: Any
    media_bundle_asset: Any
    image_asset: Any
    text_asset: Any
    lead_form_asset: Any
    book_on_google_asset: Any
    promotion_asset: Any
    callout_asset: Any
    structured_snippet_asset: Any
    sitelink_asset: Any

class AssetPolicySummary(proto.Message):
    policy_topic_entries: Any
    review_status: Any
    approval_status: Any

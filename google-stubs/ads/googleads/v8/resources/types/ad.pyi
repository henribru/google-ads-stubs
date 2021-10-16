from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    ad_type_infos as ad_type_infos,
    custom_parameter as custom_parameter,
    final_app_url as final_app_url,
    url_collection as url_collection,
)
from google.ads.googleads.v8.enums.types import (
    ad_type as ad_type,
    device as device,
    system_managed_entity_source as system_managed_entity_source,
)

__protobuf__: Any

class Ad(proto.Message):
    resource_name: Any
    id: Any
    final_urls: Any
    final_app_urls: Any
    final_mobile_urls: Any
    tracking_url_template: Any
    final_url_suffix: Any
    url_custom_parameters: Any
    display_url: Any
    type_: Any
    added_by_google_ads: Any
    device_preference: Any
    url_collections: Any
    name: Any
    system_managed_resource_source: Any
    text_ad: Any
    expanded_text_ad: Any
    call_ad: Any
    expanded_dynamic_search_ad: Any
    hotel_ad: Any
    shopping_smart_ad: Any
    shopping_product_ad: Any
    gmail_ad: Any
    image_ad: Any
    video_ad: Any
    video_responsive_ad: Any
    responsive_search_ad: Any
    legacy_responsive_display_ad: Any
    app_ad: Any
    legacy_app_install_ad: Any
    responsive_display_ad: Any
    local_ad: Any
    display_upload_ad: Any
    app_engagement_ad: Any
    shopping_comparison_listing_ad: Any
    smart_campaign_ad: Any

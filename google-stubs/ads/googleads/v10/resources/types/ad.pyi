import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import (
    ad_type_infos as ad_type_infos,
    custom_parameter as custom_parameter,
    final_app_url as final_app_url,
    url_collection as url_collection,
)
from google.ads.googleads.v10.enums.types import (
    ad_type as ad_type,
    device as device,
    system_managed_entity_source as system_managed_entity_source,
)

__protobuf__: Incomplete

class Ad(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    final_urls: Incomplete
    final_app_urls: Incomplete
    final_mobile_urls: Incomplete
    tracking_url_template: Incomplete
    final_url_suffix: Incomplete
    url_custom_parameters: Incomplete
    display_url: Incomplete
    type_: Incomplete
    added_by_google_ads: Incomplete
    device_preference: Incomplete
    url_collections: Incomplete
    name: Incomplete
    system_managed_resource_source: Incomplete
    text_ad: Incomplete
    expanded_text_ad: Incomplete
    call_ad: Incomplete
    expanded_dynamic_search_ad: Incomplete
    hotel_ad: Incomplete
    shopping_smart_ad: Incomplete
    shopping_product_ad: Incomplete
    gmail_ad: Incomplete
    image_ad: Incomplete
    video_ad: Incomplete
    video_responsive_ad: Incomplete
    responsive_search_ad: Incomplete
    legacy_responsive_display_ad: Incomplete
    app_ad: Incomplete
    legacy_app_install_ad: Incomplete
    responsive_display_ad: Incomplete
    local_ad: Incomplete
    display_upload_ad: Incomplete
    app_engagement_ad: Incomplete
    shopping_comparison_listing_ad: Incomplete
    smart_campaign_ad: Incomplete
    app_pre_registration_ad: Incomplete
    discovery_multi_asset_ad: Incomplete
    discovery_carousel_ad: Incomplete

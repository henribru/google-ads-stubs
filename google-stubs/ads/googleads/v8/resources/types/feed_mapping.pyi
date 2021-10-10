from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    ad_customizer_placeholder_field as ad_customizer_placeholder_field,
    affiliate_location_placeholder_field as affiliate_location_placeholder_field,
    app_placeholder_field as app_placeholder_field,
    call_placeholder_field as call_placeholder_field,
    callout_placeholder_field as callout_placeholder_field,
    custom_placeholder_field as custom_placeholder_field,
    dsa_page_feed_criterion_field as dsa_page_feed_criterion_field,
    education_placeholder_field as education_placeholder_field,
    feed_mapping_criterion_type as feed_mapping_criterion_type,
    feed_mapping_status as feed_mapping_status,
    flight_placeholder_field as flight_placeholder_field,
    hotel_placeholder_field as hotel_placeholder_field,
    image_placeholder_field as image_placeholder_field,
    job_placeholder_field as job_placeholder_field,
    local_placeholder_field as local_placeholder_field,
    location_extension_targeting_criterion_field as location_extension_targeting_criterion_field,
    location_placeholder_field as location_placeholder_field,
    message_placeholder_field as message_placeholder_field,
    price_placeholder_field as price_placeholder_field,
    promotion_placeholder_field as promotion_placeholder_field,
    real_estate_placeholder_field as real_estate_placeholder_field,
    sitelink_placeholder_field as sitelink_placeholder_field,
    structured_snippet_placeholder_field as structured_snippet_placeholder_field,
    travel_placeholder_field as travel_placeholder_field,
)

__protobuf__: Any

class FeedMapping(proto.Message):
    resource_name: Any
    feed: Any
    attribute_field_mappings: Any
    status: Any
    placeholder_type: Any
    criterion_type: Any

class AttributeFieldMapping(proto.Message):
    feed_attribute_id: Any
    field_id: Any
    sitelink_field: Any
    call_field: Any
    app_field: Any
    location_field: Any
    affiliate_location_field: Any
    callout_field: Any
    structured_snippet_field: Any
    message_field: Any
    price_field: Any
    promotion_field: Any
    ad_customizer_field: Any
    dsa_page_feed_field: Any
    location_extension_targeting_field: Any
    education_field: Any
    flight_field: Any
    custom_field: Any
    hotel_field: Any
    real_estate_field: Any
    travel_field: Any
    local_field: Any
    job_field: Any
    image_field: Any

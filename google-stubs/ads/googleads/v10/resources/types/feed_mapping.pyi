import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
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

__protobuf__: Incomplete

class FeedMapping(proto.Message):
    resource_name: Incomplete
    feed: Incomplete
    attribute_field_mappings: Incomplete
    status: Incomplete
    placeholder_type: Incomplete
    criterion_type: Incomplete

class AttributeFieldMapping(proto.Message):
    feed_attribute_id: Incomplete
    field_id: Incomplete
    sitelink_field: Incomplete
    call_field: Incomplete
    app_field: Incomplete
    location_field: Incomplete
    affiliate_location_field: Incomplete
    callout_field: Incomplete
    structured_snippet_field: Incomplete
    message_field: Incomplete
    price_field: Incomplete
    promotion_field: Incomplete
    ad_customizer_field: Incomplete
    dsa_page_feed_field: Incomplete
    location_extension_targeting_field: Incomplete
    education_field: Incomplete
    flight_field: Incomplete
    custom_field: Incomplete
    hotel_field: Incomplete
    real_estate_field: Incomplete
    travel_field: Incomplete
    local_field: Incomplete
    job_field: Incomplete
    image_field: Incomplete

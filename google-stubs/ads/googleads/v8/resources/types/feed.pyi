from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    affiliate_location_feed_relationship_type as affiliate_location_feed_relationship_type,
    feed_attribute_type as feed_attribute_type,
    feed_origin as feed_origin,
    feed_status as feed_status,
)

__protobuf__: Any

class Feed(proto.Message):
    class PlacesLocationFeedData(proto.Message):
        class OAuthInfo(proto.Message):
            http_method: Any
            http_request_url: Any
            http_authorization_header: Any
        oauth_info: Any
        email_address: Any
        business_account_id: Any
        business_name_filter: Any
        category_filters: Any
        label_filters: Any
    class AffiliateLocationFeedData(proto.Message):
        chain_ids: Any
        relationship_type: Any
    resource_name: Any
    id: Any
    name: Any
    attributes: Any
    attribute_operations: Any
    origin: Any
    status: Any
    places_location_feed_data: Any
    affiliate_location_feed_data: Any

class FeedAttribute(proto.Message):
    id: Any
    name: Any
    type_: Any
    is_part_of_key: Any

class FeedAttributeOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
    operator: Any
    value: Any

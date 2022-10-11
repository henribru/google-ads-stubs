import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    affiliate_location_feed_relationship_type as affiliate_location_feed_relationship_type,
    feed_attribute_type as feed_attribute_type,
    feed_origin as feed_origin,
    feed_status as feed_status,
)

__protobuf__: Incomplete

class Feed(proto.Message):
    class PlacesLocationFeedData(proto.Message):
        class OAuthInfo(proto.Message):
            http_method: Incomplete
            http_request_url: Incomplete
            http_authorization_header: Incomplete
        oauth_info: Incomplete
        email_address: Incomplete
        business_account_id: Incomplete
        business_name_filter: Incomplete
        category_filters: Incomplete
        label_filters: Incomplete

    class AffiliateLocationFeedData(proto.Message):
        chain_ids: Incomplete
        relationship_type: Incomplete
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    attributes: Incomplete
    attribute_operations: Incomplete
    origin: Incomplete
    status: Incomplete
    places_location_feed_data: Incomplete
    affiliate_location_feed_data: Incomplete

class FeedAttribute(proto.Message):
    id: Incomplete
    name: Incomplete
    type_: Incomplete
    is_part_of_key: Incomplete

class FeedAttributeOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
    operator: Incomplete
    value: Incomplete

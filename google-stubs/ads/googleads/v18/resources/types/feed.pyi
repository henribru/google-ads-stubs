import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import affiliate_location_feed_relationship_type, feed_attribute_type, feed_origin, feed_status
from typing import MutableSequence

__protobuf__: Incomplete

class Feed(proto.Message):
    class PlacesLocationFeedData(proto.Message):
        class OAuthInfo(proto.Message):
            http_method: str
            http_request_url: str
            http_authorization_header: str
        oauth_info: Feed.PlacesLocationFeedData.OAuthInfo
        email_address: str
        business_account_id: str
        business_name_filter: str
        category_filters: MutableSequence[str]
        label_filters: MutableSequence[str]
    class AffiliateLocationFeedData(proto.Message):
        chain_ids: MutableSequence[int]
        relationship_type: affiliate_location_feed_relationship_type.AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
    resource_name: str
    id: int
    name: str
    attributes: MutableSequence['FeedAttribute']
    attribute_operations: MutableSequence['FeedAttributeOperation']
    origin: feed_origin.FeedOriginEnum.FeedOrigin
    status: feed_status.FeedStatusEnum.FeedStatus
    places_location_feed_data: PlacesLocationFeedData
    affiliate_location_feed_data: AffiliateLocationFeedData

class FeedAttribute(proto.Message):
    id: int
    name: str
    type_: feed_attribute_type.FeedAttributeTypeEnum.FeedAttributeType
    is_part_of_key: bool

class FeedAttributeOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
    operator: Operator
    value: FeedAttribute

from typing import Any

import proto

from google.ads.googleads.v11.enums.types.affiliate_location_feed_relationship_type import (
    AffiliateLocationFeedRelationshipTypeEnum,
)
from google.ads.googleads.v11.enums.types.feed_attribute_type import (
    FeedAttributeTypeEnum,
)
from google.ads.googleads.v11.enums.types.feed_origin import FeedOriginEnum
from google.ads.googleads.v11.enums.types.feed_status import FeedStatusEnum

class Feed(proto.Message):
    class AffiliateLocationFeedData(proto.Message):
        chain_ids: list[int]
        relationship_type: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            chain_ids: list[int] = ...,
            relationship_type: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType = ...
        ) -> None: ...

    class PlacesLocationFeedData(proto.Message):
        class OAuthInfo(proto.Message):
            http_method: str
            http_request_url: str
            http_authorization_header: str
            def __init__(
                self,
                mapping: Any | None = ...,
                *,
                ignore_unknown_fields: bool = ...,
                http_method: str = ...,
                http_request_url: str = ...,
                http_authorization_header: str = ...
            ) -> None: ...
        oauth_info: Feed.PlacesLocationFeedData.OAuthInfo
        email_address: str
        business_account_id: str
        business_name_filter: str
        category_filters: list[str]
        label_filters: list[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            oauth_info: Feed.PlacesLocationFeedData.OAuthInfo = ...,
            email_address: str = ...,
            business_account_id: str = ...,
            business_name_filter: str = ...,
            category_filters: list[str] = ...,
            label_filters: list[str] = ...
        ) -> None: ...
    resource_name: str
    id: int
    name: str
    attributes: list[FeedAttribute]
    attribute_operations: list[FeedAttributeOperation]
    origin: FeedOriginEnum.FeedOrigin
    status: FeedStatusEnum.FeedStatus
    places_location_feed_data: Feed.PlacesLocationFeedData
    affiliate_location_feed_data: Feed.AffiliateLocationFeedData
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        attributes: list[FeedAttribute] = ...,
        attribute_operations: list[FeedAttributeOperation] = ...,
        origin: FeedOriginEnum.FeedOrigin = ...,
        status: FeedStatusEnum.FeedStatus = ...,
        places_location_feed_data: Feed.PlacesLocationFeedData = ...,
        affiliate_location_feed_data: Feed.AffiliateLocationFeedData = ...
    ) -> None: ...

class FeedAttribute(proto.Message):
    id: int
    name: str
    type_: FeedAttributeTypeEnum.FeedAttributeType
    is_part_of_key: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        id: int = ...,
        name: str = ...,
        type_: FeedAttributeTypeEnum.FeedAttributeType = ...,
        is_part_of_key: bool = ...
    ) -> None: ...

class FeedAttributeOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
    operator: FeedAttributeOperation.Operator
    value: FeedAttribute
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: FeedAttributeOperation.Operator = ...,
        value: FeedAttribute = ...
    ) -> None: ...

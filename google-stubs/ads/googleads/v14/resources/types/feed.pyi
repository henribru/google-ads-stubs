from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.affiliate_location_feed_relationship_type import (
    AffiliateLocationFeedRelationshipTypeEnum,
)
from google.ads.googleads.v14.enums.types.feed_attribute_type import (
    FeedAttributeTypeEnum,
)
from google.ads.googleads.v14.enums.types.feed_origin import FeedOriginEnum
from google.ads.googleads.v14.enums.types.feed_status import FeedStatusEnum

_M = TypeVar("_M")

class Feed(proto.Message):
    class AffiliateLocationFeedData(proto.Message):
        chain_ids: MutableSequence[int]
        relationship_type: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            chain_ids: MutableSequence[int] = ...,
            relationship_type: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["chain_ids", "relationship_type"]
        ) -> bool: ...

    class PlacesLocationFeedData(proto.Message):
        class OAuthInfo(proto.Message):
            http_method: str
            http_request_url: str
            http_authorization_header: str
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                http_method: str = ...,
                http_request_url: str = ...,
                http_authorization_header: str = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "http_method", "http_request_url", "http_authorization_header"
                ],
            ) -> bool: ...

        oauth_info: Feed.PlacesLocationFeedData.OAuthInfo
        email_address: str
        business_account_id: str
        business_name_filter: str
        category_filters: MutableSequence[str]
        label_filters: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            oauth_info: Feed.PlacesLocationFeedData.OAuthInfo = ...,
            email_address: str = ...,
            business_account_id: str = ...,
            business_name_filter: str = ...,
            category_filters: MutableSequence[str] = ...,
            label_filters: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "oauth_info",
                "email_address",
                "business_account_id",
                "business_name_filter",
                "category_filters",
                "label_filters",
            ],
        ) -> bool: ...

    resource_name: str
    id: int
    name: str
    attributes: MutableSequence[FeedAttribute]
    attribute_operations: MutableSequence[FeedAttributeOperation]
    origin: FeedOriginEnum.FeedOrigin
    status: FeedStatusEnum.FeedStatus
    places_location_feed_data: Feed.PlacesLocationFeedData
    affiliate_location_feed_data: Feed.AffiliateLocationFeedData
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        attributes: MutableSequence[FeedAttribute] = ...,
        attribute_operations: MutableSequence[FeedAttributeOperation] = ...,
        origin: FeedOriginEnum.FeedOrigin = ...,
        status: FeedStatusEnum.FeedStatus = ...,
        places_location_feed_data: Feed.PlacesLocationFeedData = ...,
        affiliate_location_feed_data: Feed.AffiliateLocationFeedData = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "name",
            "attributes",
            "attribute_operations",
            "origin",
            "status",
            "places_location_feed_data",
            "affiliate_location_feed_data",
        ],
    ) -> bool: ...

class FeedAttribute(proto.Message):
    id: int
    name: str
    type_: FeedAttributeTypeEnum.FeedAttributeType
    is_part_of_key: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: int = ...,
        name: str = ...,
        type_: FeedAttributeTypeEnum.FeedAttributeType = ...,
        is_part_of_key: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["id", "name", "type_", "is_part_of_key"]
    ) -> bool: ...

class FeedAttributeOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2

    operator: FeedAttributeOperation.Operator
    value: FeedAttribute
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: FeedAttributeOperation.Operator = ...,
        value: FeedAttribute = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "value"]
    ) -> bool: ...

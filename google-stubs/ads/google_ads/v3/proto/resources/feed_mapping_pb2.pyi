# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.enums.ad_customizer_placeholder_field_pb2 import (
    AdCustomizerPlaceholderFieldEnum as google___ads___googleads___v3___enums___ad_customizer_placeholder_field_pb2___AdCustomizerPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.affiliate_location_placeholder_field_pb2 import (
    AffiliateLocationPlaceholderFieldEnum as google___ads___googleads___v3___enums___affiliate_location_placeholder_field_pb2___AffiliateLocationPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.app_placeholder_field_pb2 import (
    AppPlaceholderFieldEnum as google___ads___googleads___v3___enums___app_placeholder_field_pb2___AppPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.call_placeholder_field_pb2 import (
    CallPlaceholderFieldEnum as google___ads___googleads___v3___enums___call_placeholder_field_pb2___CallPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.callout_placeholder_field_pb2 import (
    CalloutPlaceholderFieldEnum as google___ads___googleads___v3___enums___callout_placeholder_field_pb2___CalloutPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.custom_placeholder_field_pb2 import (
    CustomPlaceholderFieldEnum as google___ads___googleads___v3___enums___custom_placeholder_field_pb2___CustomPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.dsa_page_feed_criterion_field_pb2 import (
    DsaPageFeedCriterionFieldEnum as google___ads___googleads___v3___enums___dsa_page_feed_criterion_field_pb2___DsaPageFeedCriterionFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.education_placeholder_field_pb2 import (
    EducationPlaceholderFieldEnum as google___ads___googleads___v3___enums___education_placeholder_field_pb2___EducationPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.feed_mapping_criterion_type_pb2 import (
    FeedMappingCriterionTypeEnum as google___ads___googleads___v3___enums___feed_mapping_criterion_type_pb2___FeedMappingCriterionTypeEnum,
)
from google.ads.google_ads.v3.proto.enums.feed_mapping_status_pb2 import (
    FeedMappingStatusEnum as google___ads___googleads___v3___enums___feed_mapping_status_pb2___FeedMappingStatusEnum,
)
from google.ads.google_ads.v3.proto.enums.flight_placeholder_field_pb2 import (
    FlightPlaceholderFieldEnum as google___ads___googleads___v3___enums___flight_placeholder_field_pb2___FlightPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.hotel_placeholder_field_pb2 import (
    HotelPlaceholderFieldEnum as google___ads___googleads___v3___enums___hotel_placeholder_field_pb2___HotelPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.job_placeholder_field_pb2 import (
    JobPlaceholderFieldEnum as google___ads___googleads___v3___enums___job_placeholder_field_pb2___JobPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.local_placeholder_field_pb2 import (
    LocalPlaceholderFieldEnum as google___ads___googleads___v3___enums___local_placeholder_field_pb2___LocalPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.location_extension_targeting_criterion_field_pb2 import (
    LocationExtensionTargetingCriterionFieldEnum as google___ads___googleads___v3___enums___location_extension_targeting_criterion_field_pb2___LocationExtensionTargetingCriterionFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.location_placeholder_field_pb2 import (
    LocationPlaceholderFieldEnum as google___ads___googleads___v3___enums___location_placeholder_field_pb2___LocationPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.message_placeholder_field_pb2 import (
    MessagePlaceholderFieldEnum as google___ads___googleads___v3___enums___message_placeholder_field_pb2___MessagePlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.placeholder_type_pb2 import (
    PlaceholderTypeEnum as google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum,
)
from google.ads.google_ads.v3.proto.enums.price_placeholder_field_pb2 import (
    PricePlaceholderFieldEnum as google___ads___googleads___v3___enums___price_placeholder_field_pb2___PricePlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.promotion_placeholder_field_pb2 import (
    PromotionPlaceholderFieldEnum as google___ads___googleads___v3___enums___promotion_placeholder_field_pb2___PromotionPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.real_estate_placeholder_field_pb2 import (
    RealEstatePlaceholderFieldEnum as google___ads___googleads___v3___enums___real_estate_placeholder_field_pb2___RealEstatePlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.sitelink_placeholder_field_pb2 import (
    SitelinkPlaceholderFieldEnum as google___ads___googleads___v3___enums___sitelink_placeholder_field_pb2___SitelinkPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.structured_snippet_placeholder_field_pb2 import (
    StructuredSnippetPlaceholderFieldEnum as google___ads___googleads___v3___enums___structured_snippet_placeholder_field_pb2___StructuredSnippetPlaceholderFieldEnum,
)
from google.ads.google_ads.v3.proto.enums.travel_placeholder_field_pb2 import (
    TravelPlaceholderFieldEnum as google___ads___googleads___v3___enums___travel_placeholder_field_pb2___TravelPlaceholderFieldEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeedMapping(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v3___enums___feed_mapping_status_pb2___FeedMappingStatusEnum.FeedMappingStatusValue = ...
    placeholder_type: google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue = ...
    criterion_type: google___ads___googleads___v3___enums___feed_mapping_criterion_type_pb2___FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue = ...
    @property
    def feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def attribute_field_mappings(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___AttributeFieldMapping
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        feed: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        attribute_field_mappings: typing___Optional[
            typing___Iterable[type___AttributeFieldMapping]
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v3___enums___feed_mapping_status_pb2___FeedMappingStatusEnum.FeedMappingStatusValue
        ] = None,
        placeholder_type: typing___Optional[
            google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue
        ] = None,
        criterion_type: typing___Optional[
            google___ads___googleads___v3___enums___feed_mapping_criterion_type_pb2___FeedMappingCriterionTypeEnum.FeedMappingCriterionTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "criterion_type",
            b"criterion_type",
            "feed",
            b"feed",
            "placeholder_type",
            b"placeholder_type",
            "target",
            b"target",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "attribute_field_mappings",
            b"attribute_field_mappings",
            "criterion_type",
            b"criterion_type",
            "feed",
            b"feed",
            "placeholder_type",
            b"placeholder_type",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "target",
            b"target",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["target", b"target"]
    ) -> typing_extensions___Literal["placeholder_type", "criterion_type"]: ...

type___FeedMapping = FeedMapping

class AttributeFieldMapping(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sitelink_field: google___ads___googleads___v3___enums___sitelink_placeholder_field_pb2___SitelinkPlaceholderFieldEnum.SitelinkPlaceholderFieldValue = ...
    call_field: google___ads___googleads___v3___enums___call_placeholder_field_pb2___CallPlaceholderFieldEnum.CallPlaceholderFieldValue = ...
    app_field: google___ads___googleads___v3___enums___app_placeholder_field_pb2___AppPlaceholderFieldEnum.AppPlaceholderFieldValue = ...
    location_field: google___ads___googleads___v3___enums___location_placeholder_field_pb2___LocationPlaceholderFieldEnum.LocationPlaceholderFieldValue = ...
    affiliate_location_field: google___ads___googleads___v3___enums___affiliate_location_placeholder_field_pb2___AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderFieldValue = ...
    callout_field: google___ads___googleads___v3___enums___callout_placeholder_field_pb2___CalloutPlaceholderFieldEnum.CalloutPlaceholderFieldValue = ...
    structured_snippet_field: google___ads___googleads___v3___enums___structured_snippet_placeholder_field_pb2___StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue = ...
    message_field: google___ads___googleads___v3___enums___message_placeholder_field_pb2___MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue = ...
    price_field: google___ads___googleads___v3___enums___price_placeholder_field_pb2___PricePlaceholderFieldEnum.PricePlaceholderFieldValue = ...
    promotion_field: google___ads___googleads___v3___enums___promotion_placeholder_field_pb2___PromotionPlaceholderFieldEnum.PromotionPlaceholderFieldValue = ...
    ad_customizer_field: google___ads___googleads___v3___enums___ad_customizer_placeholder_field_pb2___AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderFieldValue = ...
    dsa_page_feed_field: google___ads___googleads___v3___enums___dsa_page_feed_criterion_field_pb2___DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionFieldValue = ...
    location_extension_targeting_field: google___ads___googleads___v3___enums___location_extension_targeting_criterion_field_pb2___LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue = ...
    education_field: google___ads___googleads___v3___enums___education_placeholder_field_pb2___EducationPlaceholderFieldEnum.EducationPlaceholderFieldValue = ...
    flight_field: google___ads___googleads___v3___enums___flight_placeholder_field_pb2___FlightPlaceholderFieldEnum.FlightPlaceholderFieldValue = ...
    custom_field: google___ads___googleads___v3___enums___custom_placeholder_field_pb2___CustomPlaceholderFieldEnum.CustomPlaceholderFieldValue = ...
    hotel_field: google___ads___googleads___v3___enums___hotel_placeholder_field_pb2___HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue = ...
    real_estate_field: google___ads___googleads___v3___enums___real_estate_placeholder_field_pb2___RealEstatePlaceholderFieldEnum.RealEstatePlaceholderFieldValue = ...
    travel_field: google___ads___googleads___v3___enums___travel_placeholder_field_pb2___TravelPlaceholderFieldEnum.TravelPlaceholderFieldValue = ...
    local_field: google___ads___googleads___v3___enums___local_placeholder_field_pb2___LocalPlaceholderFieldEnum.LocalPlaceholderFieldValue = ...
    job_field: google___ads___googleads___v3___enums___job_placeholder_field_pb2___JobPlaceholderFieldEnum.JobPlaceholderFieldValue = ...
    @property
    def feed_attribute_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def field_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        feed_attribute_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        field_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        sitelink_field: typing___Optional[
            google___ads___googleads___v3___enums___sitelink_placeholder_field_pb2___SitelinkPlaceholderFieldEnum.SitelinkPlaceholderFieldValue
        ] = None,
        call_field: typing___Optional[
            google___ads___googleads___v3___enums___call_placeholder_field_pb2___CallPlaceholderFieldEnum.CallPlaceholderFieldValue
        ] = None,
        app_field: typing___Optional[
            google___ads___googleads___v3___enums___app_placeholder_field_pb2___AppPlaceholderFieldEnum.AppPlaceholderFieldValue
        ] = None,
        location_field: typing___Optional[
            google___ads___googleads___v3___enums___location_placeholder_field_pb2___LocationPlaceholderFieldEnum.LocationPlaceholderFieldValue
        ] = None,
        affiliate_location_field: typing___Optional[
            google___ads___googleads___v3___enums___affiliate_location_placeholder_field_pb2___AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderFieldValue
        ] = None,
        callout_field: typing___Optional[
            google___ads___googleads___v3___enums___callout_placeholder_field_pb2___CalloutPlaceholderFieldEnum.CalloutPlaceholderFieldValue
        ] = None,
        structured_snippet_field: typing___Optional[
            google___ads___googleads___v3___enums___structured_snippet_placeholder_field_pb2___StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue
        ] = None,
        message_field: typing___Optional[
            google___ads___googleads___v3___enums___message_placeholder_field_pb2___MessagePlaceholderFieldEnum.MessagePlaceholderFieldValue
        ] = None,
        price_field: typing___Optional[
            google___ads___googleads___v3___enums___price_placeholder_field_pb2___PricePlaceholderFieldEnum.PricePlaceholderFieldValue
        ] = None,
        promotion_field: typing___Optional[
            google___ads___googleads___v3___enums___promotion_placeholder_field_pb2___PromotionPlaceholderFieldEnum.PromotionPlaceholderFieldValue
        ] = None,
        ad_customizer_field: typing___Optional[
            google___ads___googleads___v3___enums___ad_customizer_placeholder_field_pb2___AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderFieldValue
        ] = None,
        dsa_page_feed_field: typing___Optional[
            google___ads___googleads___v3___enums___dsa_page_feed_criterion_field_pb2___DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionFieldValue
        ] = None,
        location_extension_targeting_field: typing___Optional[
            google___ads___googleads___v3___enums___location_extension_targeting_criterion_field_pb2___LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue
        ] = None,
        education_field: typing___Optional[
            google___ads___googleads___v3___enums___education_placeholder_field_pb2___EducationPlaceholderFieldEnum.EducationPlaceholderFieldValue
        ] = None,
        flight_field: typing___Optional[
            google___ads___googleads___v3___enums___flight_placeholder_field_pb2___FlightPlaceholderFieldEnum.FlightPlaceholderFieldValue
        ] = None,
        custom_field: typing___Optional[
            google___ads___googleads___v3___enums___custom_placeholder_field_pb2___CustomPlaceholderFieldEnum.CustomPlaceholderFieldValue
        ] = None,
        hotel_field: typing___Optional[
            google___ads___googleads___v3___enums___hotel_placeholder_field_pb2___HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue
        ] = None,
        real_estate_field: typing___Optional[
            google___ads___googleads___v3___enums___real_estate_placeholder_field_pb2___RealEstatePlaceholderFieldEnum.RealEstatePlaceholderFieldValue
        ] = None,
        travel_field: typing___Optional[
            google___ads___googleads___v3___enums___travel_placeholder_field_pb2___TravelPlaceholderFieldEnum.TravelPlaceholderFieldValue
        ] = None,
        local_field: typing___Optional[
            google___ads___googleads___v3___enums___local_placeholder_field_pb2___LocalPlaceholderFieldEnum.LocalPlaceholderFieldValue
        ] = None,
        job_field: typing___Optional[
            google___ads___googleads___v3___enums___job_placeholder_field_pb2___JobPlaceholderFieldEnum.JobPlaceholderFieldValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_customizer_field",
            b"ad_customizer_field",
            "affiliate_location_field",
            b"affiliate_location_field",
            "app_field",
            b"app_field",
            "call_field",
            b"call_field",
            "callout_field",
            b"callout_field",
            "custom_field",
            b"custom_field",
            "dsa_page_feed_field",
            b"dsa_page_feed_field",
            "education_field",
            b"education_field",
            "feed_attribute_id",
            b"feed_attribute_id",
            "field",
            b"field",
            "field_id",
            b"field_id",
            "flight_field",
            b"flight_field",
            "hotel_field",
            b"hotel_field",
            "job_field",
            b"job_field",
            "local_field",
            b"local_field",
            "location_extension_targeting_field",
            b"location_extension_targeting_field",
            "location_field",
            b"location_field",
            "message_field",
            b"message_field",
            "price_field",
            b"price_field",
            "promotion_field",
            b"promotion_field",
            "real_estate_field",
            b"real_estate_field",
            "sitelink_field",
            b"sitelink_field",
            "structured_snippet_field",
            b"structured_snippet_field",
            "travel_field",
            b"travel_field",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_customizer_field",
            b"ad_customizer_field",
            "affiliate_location_field",
            b"affiliate_location_field",
            "app_field",
            b"app_field",
            "call_field",
            b"call_field",
            "callout_field",
            b"callout_field",
            "custom_field",
            b"custom_field",
            "dsa_page_feed_field",
            b"dsa_page_feed_field",
            "education_field",
            b"education_field",
            "feed_attribute_id",
            b"feed_attribute_id",
            "field",
            b"field",
            "field_id",
            b"field_id",
            "flight_field",
            b"flight_field",
            "hotel_field",
            b"hotel_field",
            "job_field",
            b"job_field",
            "local_field",
            b"local_field",
            "location_extension_targeting_field",
            b"location_extension_targeting_field",
            "location_field",
            b"location_field",
            "message_field",
            b"message_field",
            "price_field",
            b"price_field",
            "promotion_field",
            b"promotion_field",
            "real_estate_field",
            b"real_estate_field",
            "sitelink_field",
            b"sitelink_field",
            "structured_snippet_field",
            b"structured_snippet_field",
            "travel_field",
            b"travel_field",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["field", b"field"]
    ) -> typing_extensions___Literal[
        "sitelink_field",
        "call_field",
        "app_field",
        "location_field",
        "affiliate_location_field",
        "callout_field",
        "structured_snippet_field",
        "message_field",
        "price_field",
        "promotion_field",
        "ad_customizer_field",
        "dsa_page_feed_field",
        "location_extension_targeting_field",
        "education_field",
        "flight_field",
        "custom_field",
        "hotel_field",
        "real_estate_field",
        "travel_field",
        "local_field",
        "job_field",
    ]: ...

type___AttributeFieldMapping = AttributeFieldMapping

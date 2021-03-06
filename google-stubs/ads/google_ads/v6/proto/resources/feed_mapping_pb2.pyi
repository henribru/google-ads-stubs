"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.enums.ad_customizer_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.affiliate_location_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.app_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.call_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.callout_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.custom_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.dsa_page_feed_criterion_field_pb2
import google.ads.google_ads.v6.proto.enums.education_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.feed_mapping_criterion_type_pb2
import google.ads.google_ads.v6.proto.enums.feed_mapping_status_pb2
import google.ads.google_ads.v6.proto.enums.flight_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.hotel_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.image_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.job_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.local_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.location_extension_targeting_criterion_field_pb2
import google.ads.google_ads.v6.proto.enums.location_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.message_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.placeholder_type_pb2
import google.ads.google_ads.v6.proto.enums.price_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.promotion_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.real_estate_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.sitelink_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.structured_snippet_placeholder_field_pb2
import google.ads.google_ads.v6.proto.enums.travel_placeholder_field_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeedMapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    FEED_FIELD_NUMBER: builtins.int
    ATTRIBUTE_FIELD_MAPPINGS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PLACEHOLDER_TYPE_FIELD_NUMBER: builtins.int
    CRITERION_TYPE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    feed: typing.Text = ...
    status: google.ads.google_ads.v6.proto.enums.feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus.V = (
        ...
    )
    placeholder_type: google.ads.google_ads.v6.proto.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.V = (
        ...
    )
    criterion_type: google.ads.google_ads.v6.proto.enums.feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType.V = (
        ...
    )
    @property
    def attribute_field_mappings(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___AttributeFieldMapping
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        feed: typing.Text = ...,
        attribute_field_mappings: typing.Optional[
            typing.Iterable[global___AttributeFieldMapping]
        ] = ...,
        status: google.ads.google_ads.v6.proto.enums.feed_mapping_status_pb2.FeedMappingStatusEnum.FeedMappingStatus.V = ...,
        placeholder_type: google.ads.google_ads.v6.proto.enums.placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType.V = ...,
        criterion_type: google.ads.google_ads.v6.proto.enums.feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum.FeedMappingCriterionType.V = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_feed",
            b"_feed",
            "criterion_type",
            b"criterion_type",
            "feed",
            b"feed",
            "placeholder_type",
            b"placeholder_type",
            "target",
            b"target",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_feed",
            b"_feed",
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
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_feed", b"_feed"]
    ) -> typing_extensions.Literal["feed"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["target", b"target"]
    ) -> typing_extensions.Literal["placeholder_type", "criterion_type"]: ...

global___FeedMapping = FeedMapping

class AttributeFieldMapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FEED_ATTRIBUTE_ID_FIELD_NUMBER: builtins.int
    FIELD_ID_FIELD_NUMBER: builtins.int
    SITELINK_FIELD_FIELD_NUMBER: builtins.int
    CALL_FIELD_FIELD_NUMBER: builtins.int
    APP_FIELD_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_FIELD_NUMBER: builtins.int
    AFFILIATE_LOCATION_FIELD_FIELD_NUMBER: builtins.int
    CALLOUT_FIELD_FIELD_NUMBER: builtins.int
    STRUCTURED_SNIPPET_FIELD_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_FIELD_NUMBER: builtins.int
    PRICE_FIELD_FIELD_NUMBER: builtins.int
    PROMOTION_FIELD_FIELD_NUMBER: builtins.int
    AD_CUSTOMIZER_FIELD_FIELD_NUMBER: builtins.int
    DSA_PAGE_FEED_FIELD_FIELD_NUMBER: builtins.int
    LOCATION_EXTENSION_TARGETING_FIELD_FIELD_NUMBER: builtins.int
    EDUCATION_FIELD_FIELD_NUMBER: builtins.int
    FLIGHT_FIELD_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_FIELD_NUMBER: builtins.int
    HOTEL_FIELD_FIELD_NUMBER: builtins.int
    REAL_ESTATE_FIELD_FIELD_NUMBER: builtins.int
    TRAVEL_FIELD_FIELD_NUMBER: builtins.int
    LOCAL_FIELD_FIELD_NUMBER: builtins.int
    JOB_FIELD_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_FIELD_NUMBER: builtins.int
    feed_attribute_id: builtins.int = ...
    field_id: builtins.int = ...
    sitelink_field: google.ads.google_ads.v6.proto.enums.sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V = (
        ...
    )
    call_field: google.ads.google_ads.v6.proto.enums.call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField.V = (
        ...
    )
    app_field: google.ads.google_ads.v6.proto.enums.app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField.V = (
        ...
    )
    location_field: google.ads.google_ads.v6.proto.enums.location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField.V = (
        ...
    )
    affiliate_location_field: google.ads.google_ads.v6.proto.enums.affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField.V = (
        ...
    )
    callout_field: google.ads.google_ads.v6.proto.enums.callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField.V = (
        ...
    )
    structured_snippet_field: google.ads.google_ads.v6.proto.enums.structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V = (
        ...
    )
    message_field: google.ads.google_ads.v6.proto.enums.message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField.V = (
        ...
    )
    price_field: google.ads.google_ads.v6.proto.enums.price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField.V = (
        ...
    )
    promotion_field: google.ads.google_ads.v6.proto.enums.promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField.V = (
        ...
    )
    ad_customizer_field: google.ads.google_ads.v6.proto.enums.ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.V = (
        ...
    )
    dsa_page_feed_field: google.ads.google_ads.v6.proto.enums.dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V = (
        ...
    )
    location_extension_targeting_field: google.ads.google_ads.v6.proto.enums.location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField.V = (
        ...
    )
    education_field: google.ads.google_ads.v6.proto.enums.education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField.V = (
        ...
    )
    flight_field: google.ads.google_ads.v6.proto.enums.flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField.V = (
        ...
    )
    custom_field: google.ads.google_ads.v6.proto.enums.custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField.V = (
        ...
    )
    hotel_field: google.ads.google_ads.v6.proto.enums.hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField.V = (
        ...
    )
    real_estate_field: google.ads.google_ads.v6.proto.enums.real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField.V = (
        ...
    )
    travel_field: google.ads.google_ads.v6.proto.enums.travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField.V = (
        ...
    )
    local_field: google.ads.google_ads.v6.proto.enums.local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField.V = (
        ...
    )
    job_field: google.ads.google_ads.v6.proto.enums.job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField.V = (
        ...
    )
    image_field: google.ads.google_ads.v6.proto.enums.image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField.V = (
        ...
    )
    def __init__(
        self,
        *,
        feed_attribute_id: builtins.int = ...,
        field_id: builtins.int = ...,
        sitelink_field: google.ads.google_ads.v6.proto.enums.sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V = ...,
        call_field: google.ads.google_ads.v6.proto.enums.call_placeholder_field_pb2.CallPlaceholderFieldEnum.CallPlaceholderField.V = ...,
        app_field: google.ads.google_ads.v6.proto.enums.app_placeholder_field_pb2.AppPlaceholderFieldEnum.AppPlaceholderField.V = ...,
        location_field: google.ads.google_ads.v6.proto.enums.location_placeholder_field_pb2.LocationPlaceholderFieldEnum.LocationPlaceholderField.V = ...,
        affiliate_location_field: google.ads.google_ads.v6.proto.enums.affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField.V = ...,
        callout_field: google.ads.google_ads.v6.proto.enums.callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum.CalloutPlaceholderField.V = ...,
        structured_snippet_field: google.ads.google_ads.v6.proto.enums.structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V = ...,
        message_field: google.ads.google_ads.v6.proto.enums.message_placeholder_field_pb2.MessagePlaceholderFieldEnum.MessagePlaceholderField.V = ...,
        price_field: google.ads.google_ads.v6.proto.enums.price_placeholder_field_pb2.PricePlaceholderFieldEnum.PricePlaceholderField.V = ...,
        promotion_field: google.ads.google_ads.v6.proto.enums.promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum.PromotionPlaceholderField.V = ...,
        ad_customizer_field: google.ads.google_ads.v6.proto.enums.ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField.V = ...,
        dsa_page_feed_field: google.ads.google_ads.v6.proto.enums.dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V = ...,
        location_extension_targeting_field: google.ads.google_ads.v6.proto.enums.location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField.V = ...,
        education_field: google.ads.google_ads.v6.proto.enums.education_placeholder_field_pb2.EducationPlaceholderFieldEnum.EducationPlaceholderField.V = ...,
        flight_field: google.ads.google_ads.v6.proto.enums.flight_placeholder_field_pb2.FlightPlaceholderFieldEnum.FlightPlaceholderField.V = ...,
        custom_field: google.ads.google_ads.v6.proto.enums.custom_placeholder_field_pb2.CustomPlaceholderFieldEnum.CustomPlaceholderField.V = ...,
        hotel_field: google.ads.google_ads.v6.proto.enums.hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum.HotelPlaceholderField.V = ...,
        real_estate_field: google.ads.google_ads.v6.proto.enums.real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField.V = ...,
        travel_field: google.ads.google_ads.v6.proto.enums.travel_placeholder_field_pb2.TravelPlaceholderFieldEnum.TravelPlaceholderField.V = ...,
        local_field: google.ads.google_ads.v6.proto.enums.local_placeholder_field_pb2.LocalPlaceholderFieldEnum.LocalPlaceholderField.V = ...,
        job_field: google.ads.google_ads.v6.proto.enums.job_placeholder_field_pb2.JobPlaceholderFieldEnum.JobPlaceholderField.V = ...,
        image_field: google.ads.google_ads.v6.proto.enums.image_placeholder_field_pb2.ImagePlaceholderFieldEnum.ImagePlaceholderField.V = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_feed_attribute_id",
            b"_feed_attribute_id",
            "_field_id",
            b"_field_id",
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
            "image_field",
            b"image_field",
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
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_feed_attribute_id",
            b"_feed_attribute_id",
            "_field_id",
            b"_field_id",
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
            "image_field",
            b"image_field",
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
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_feed_attribute_id", b"_feed_attribute_id"
        ],
    ) -> typing_extensions.Literal["feed_attribute_id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_field_id", b"_field_id"]
    ) -> typing_extensions.Literal["field_id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["field", b"field"]
    ) -> typing_extensions.Literal[
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
        "image_field",
    ]: ...

global___AttributeFieldMapping = AttributeFieldMapping

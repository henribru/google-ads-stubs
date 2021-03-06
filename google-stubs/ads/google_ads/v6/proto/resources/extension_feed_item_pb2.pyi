"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.common.criteria_pb2
import google.ads.google_ads.v6.proto.common.extensions_pb2
import google.ads.google_ads.v6.proto.enums.extension_type_pb2
import google.ads.google_ads.v6.proto.enums.feed_item_status_pb2
import google.ads.google_ads.v6.proto.enums.feed_item_target_device_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ExtensionFeedItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    EXTENSION_TYPE_FIELD_NUMBER: builtins.int
    START_DATE_TIME_FIELD_NUMBER: builtins.int
    END_DATE_TIME_FIELD_NUMBER: builtins.int
    AD_SCHEDULES_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    TARGETED_GEO_TARGET_CONSTANT_FIELD_NUMBER: builtins.int
    TARGETED_KEYWORD_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SITELINK_FEED_ITEM_FIELD_NUMBER: builtins.int
    STRUCTURED_SNIPPET_FEED_ITEM_FIELD_NUMBER: builtins.int
    APP_FEED_ITEM_FIELD_NUMBER: builtins.int
    CALL_FEED_ITEM_FIELD_NUMBER: builtins.int
    CALLOUT_FEED_ITEM_FIELD_NUMBER: builtins.int
    TEXT_MESSAGE_FEED_ITEM_FIELD_NUMBER: builtins.int
    PRICE_FEED_ITEM_FIELD_NUMBER: builtins.int
    PROMOTION_FEED_ITEM_FIELD_NUMBER: builtins.int
    LOCATION_FEED_ITEM_FIELD_NUMBER: builtins.int
    AFFILIATE_LOCATION_FEED_ITEM_FIELD_NUMBER: builtins.int
    HOTEL_CALLOUT_FEED_ITEM_FIELD_NUMBER: builtins.int
    IMAGE_FEED_ITEM_FIELD_NUMBER: builtins.int
    TARGETED_CAMPAIGN_FIELD_NUMBER: builtins.int
    TARGETED_AD_GROUP_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    id: builtins.int = ...
    extension_type: google.ads.google_ads.v6.proto.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.V = (
        ...
    )
    start_date_time: typing.Text = ...
    end_date_time: typing.Text = ...
    device: google.ads.google_ads.v6.proto.enums.feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice.V = (
        ...
    )
    targeted_geo_target_constant: typing.Text = ...
    status: google.ads.google_ads.v6.proto.enums.feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus.V = (
        ...
    )
    targeted_campaign: typing.Text = ...
    targeted_ad_group: typing.Text = ...
    @property
    def ad_schedules(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.ads.google_ads.v6.proto.common.criteria_pb2.AdScheduleInfo
    ]: ...
    @property
    def targeted_keyword(
        self,
    ) -> google.ads.google_ads.v6.proto.common.criteria_pb2.KeywordInfo: ...
    @property
    def sitelink_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.SitelinkFeedItem: ...
    @property
    def structured_snippet_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.StructuredSnippetFeedItem: ...
    @property
    def app_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.AppFeedItem: ...
    @property
    def call_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.CallFeedItem: ...
    @property
    def callout_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.CalloutFeedItem: ...
    @property
    def text_message_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.TextMessageFeedItem: ...
    @property
    def price_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.PriceFeedItem: ...
    @property
    def promotion_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.PromotionFeedItem: ...
    @property
    def location_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.LocationFeedItem: ...
    @property
    def affiliate_location_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.AffiliateLocationFeedItem: ...
    @property
    def hotel_callout_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.HotelCalloutFeedItem: ...
    @property
    def image_feed_item(
        self,
    ) -> google.ads.google_ads.v6.proto.common.extensions_pb2.ImageFeedItem: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: builtins.int = ...,
        extension_type: google.ads.google_ads.v6.proto.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.V = ...,
        start_date_time: typing.Text = ...,
        end_date_time: typing.Text = ...,
        ad_schedules: typing.Optional[
            typing.Iterable[
                google.ads.google_ads.v6.proto.common.criteria_pb2.AdScheduleInfo
            ]
        ] = ...,
        device: google.ads.google_ads.v6.proto.enums.feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice.V = ...,
        targeted_geo_target_constant: typing.Text = ...,
        targeted_keyword: typing.Optional[
            google.ads.google_ads.v6.proto.common.criteria_pb2.KeywordInfo
        ] = ...,
        status: google.ads.google_ads.v6.proto.enums.feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus.V = ...,
        sitelink_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.SitelinkFeedItem
        ] = ...,
        structured_snippet_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.StructuredSnippetFeedItem
        ] = ...,
        app_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.AppFeedItem
        ] = ...,
        call_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.CallFeedItem
        ] = ...,
        callout_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.CalloutFeedItem
        ] = ...,
        text_message_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.TextMessageFeedItem
        ] = ...,
        price_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.PriceFeedItem
        ] = ...,
        promotion_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.PromotionFeedItem
        ] = ...,
        location_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.LocationFeedItem
        ] = ...,
        affiliate_location_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.AffiliateLocationFeedItem
        ] = ...,
        hotel_callout_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.HotelCalloutFeedItem
        ] = ...,
        image_feed_item: typing.Optional[
            google.ads.google_ads.v6.proto.common.extensions_pb2.ImageFeedItem
        ] = ...,
        targeted_campaign: typing.Text = ...,
        targeted_ad_group: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_end_date_time",
            b"_end_date_time",
            "_id",
            b"_id",
            "_start_date_time",
            b"_start_date_time",
            "_targeted_geo_target_constant",
            b"_targeted_geo_target_constant",
            "affiliate_location_feed_item",
            b"affiliate_location_feed_item",
            "app_feed_item",
            b"app_feed_item",
            "call_feed_item",
            b"call_feed_item",
            "callout_feed_item",
            b"callout_feed_item",
            "end_date_time",
            b"end_date_time",
            "extension",
            b"extension",
            "hotel_callout_feed_item",
            b"hotel_callout_feed_item",
            "id",
            b"id",
            "image_feed_item",
            b"image_feed_item",
            "location_feed_item",
            b"location_feed_item",
            "price_feed_item",
            b"price_feed_item",
            "promotion_feed_item",
            b"promotion_feed_item",
            "serving_resource_targeting",
            b"serving_resource_targeting",
            "sitelink_feed_item",
            b"sitelink_feed_item",
            "start_date_time",
            b"start_date_time",
            "structured_snippet_feed_item",
            b"structured_snippet_feed_item",
            "targeted_ad_group",
            b"targeted_ad_group",
            "targeted_campaign",
            b"targeted_campaign",
            "targeted_geo_target_constant",
            b"targeted_geo_target_constant",
            "targeted_keyword",
            b"targeted_keyword",
            "text_message_feed_item",
            b"text_message_feed_item",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_end_date_time",
            b"_end_date_time",
            "_id",
            b"_id",
            "_start_date_time",
            b"_start_date_time",
            "_targeted_geo_target_constant",
            b"_targeted_geo_target_constant",
            "ad_schedules",
            b"ad_schedules",
            "affiliate_location_feed_item",
            b"affiliate_location_feed_item",
            "app_feed_item",
            b"app_feed_item",
            "call_feed_item",
            b"call_feed_item",
            "callout_feed_item",
            b"callout_feed_item",
            "device",
            b"device",
            "end_date_time",
            b"end_date_time",
            "extension",
            b"extension",
            "extension_type",
            b"extension_type",
            "hotel_callout_feed_item",
            b"hotel_callout_feed_item",
            "id",
            b"id",
            "image_feed_item",
            b"image_feed_item",
            "location_feed_item",
            b"location_feed_item",
            "price_feed_item",
            b"price_feed_item",
            "promotion_feed_item",
            b"promotion_feed_item",
            "resource_name",
            b"resource_name",
            "serving_resource_targeting",
            b"serving_resource_targeting",
            "sitelink_feed_item",
            b"sitelink_feed_item",
            "start_date_time",
            b"start_date_time",
            "status",
            b"status",
            "structured_snippet_feed_item",
            b"structured_snippet_feed_item",
            "targeted_ad_group",
            b"targeted_ad_group",
            "targeted_campaign",
            b"targeted_campaign",
            "targeted_geo_target_constant",
            b"targeted_geo_target_constant",
            "targeted_keyword",
            b"targeted_keyword",
            "text_message_feed_item",
            b"text_message_feed_item",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_end_date_time", b"_end_date_time"],
    ) -> typing_extensions.Literal["end_date_time"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_id", b"_id"]
    ) -> typing_extensions.Literal["id"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["_start_date_time", b"_start_date_time"],
    ) -> typing_extensions.Literal["start_date_time"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_targeted_geo_target_constant", b"_targeted_geo_target_constant"
        ],
    ) -> typing_extensions.Literal["targeted_geo_target_constant"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["extension", b"extension"]
    ) -> typing_extensions.Literal[
        "sitelink_feed_item",
        "structured_snippet_feed_item",
        "app_feed_item",
        "call_feed_item",
        "callout_feed_item",
        "text_message_feed_item",
        "price_feed_item",
        "promotion_feed_item",
        "location_feed_item",
        "affiliate_location_feed_item",
        "hotel_callout_feed_item",
        "image_feed_item",
    ]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "serving_resource_targeting", b"serving_resource_targeting"
        ],
    ) -> typing_extensions.Literal["targeted_campaign", "targeted_ad_group"]: ...

global___ExtensionFeedItem = ExtensionFeedItem

# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.criteria_pb2 import (
    AdScheduleInfo as google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo,
    KeywordInfo as google___ads___googleads___v2___common___criteria_pb2___KeywordInfo,
)

from google.ads.google_ads.v2.proto.common.extensions_pb2 import (
    AffiliateLocationFeedItem as google___ads___googleads___v2___common___extensions_pb2___AffiliateLocationFeedItem,
    AppFeedItem as google___ads___googleads___v2___common___extensions_pb2___AppFeedItem,
    CallFeedItem as google___ads___googleads___v2___common___extensions_pb2___CallFeedItem,
    CalloutFeedItem as google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem,
    HotelCalloutFeedItem as google___ads___googleads___v2___common___extensions_pb2___HotelCalloutFeedItem,
    LocationFeedItem as google___ads___googleads___v2___common___extensions_pb2___LocationFeedItem,
    PriceFeedItem as google___ads___googleads___v2___common___extensions_pb2___PriceFeedItem,
    PromotionFeedItem as google___ads___googleads___v2___common___extensions_pb2___PromotionFeedItem,
    SitelinkFeedItem as google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem,
    StructuredSnippetFeedItem as google___ads___googleads___v2___common___extensions_pb2___StructuredSnippetFeedItem,
    TextMessageFeedItem as google___ads___googleads___v2___common___extensions_pb2___TextMessageFeedItem,
)

from google.ads.google_ads.v2.proto.enums.extension_type_pb2 import (
    ExtensionTypeEnum as google___ads___googleads___v2___enums___extension_type_pb2___ExtensionTypeEnum,
)

from google.ads.google_ads.v2.proto.enums.feed_item_status_pb2 import (
    FeedItemStatusEnum as google___ads___googleads___v2___enums___feed_item_status_pb2___FeedItemStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.feed_item_target_device_pb2 import (
    FeedItemTargetDeviceEnum as google___ads___googleads___v2___enums___feed_item_target_device_pb2___FeedItemTargetDeviceEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ExtensionFeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text
    extension_type = ... # type: google___ads___googleads___v2___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionType
    device = ... # type: google___ads___googleads___v2___enums___feed_item_target_device_pb2___FeedItemTargetDeviceEnum.FeedItemTargetDevice
    status = ... # type: google___ads___googleads___v2___enums___feed_item_status_pb2___FeedItemStatusEnum.FeedItemStatus

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def start_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def end_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_schedules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo]: ...

    @property
    def targeted_geo_target_constant(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def targeted_keyword(self) -> google___ads___googleads___v2___common___criteria_pb2___KeywordInfo: ...

    @property
    def sitelink_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem: ...

    @property
    def structured_snippet_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___StructuredSnippetFeedItem: ...

    @property
    def app_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___AppFeedItem: ...

    @property
    def call_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___CallFeedItem: ...

    @property
    def callout_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem: ...

    @property
    def text_message_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___TextMessageFeedItem: ...

    @property
    def price_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___PriceFeedItem: ...

    @property
    def promotion_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___PromotionFeedItem: ...

    @property
    def location_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___LocationFeedItem: ...

    @property
    def affiliate_location_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___AffiliateLocationFeedItem: ...

    @property
    def hotel_callout_feed_item(self) -> google___ads___googleads___v2___common___extensions_pb2___HotelCalloutFeedItem: ...

    @property
    def targeted_campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def targeted_ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        extension_type : typing___Optional[google___ads___googleads___v2___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionType] = None,
        start_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        end_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_schedules : typing___Optional[typing___Iterable[google___ads___googleads___v2___common___criteria_pb2___AdScheduleInfo]] = None,
        device : typing___Optional[google___ads___googleads___v2___enums___feed_item_target_device_pb2___FeedItemTargetDeviceEnum.FeedItemTargetDevice] = None,
        targeted_geo_target_constant : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        targeted_keyword : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___KeywordInfo] = None,
        status : typing___Optional[google___ads___googleads___v2___enums___feed_item_status_pb2___FeedItemStatusEnum.FeedItemStatus] = None,
        sitelink_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem] = None,
        structured_snippet_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___StructuredSnippetFeedItem] = None,
        app_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___AppFeedItem] = None,
        call_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___CallFeedItem] = None,
        callout_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem] = None,
        text_message_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___TextMessageFeedItem] = None,
        price_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___PriceFeedItem] = None,
        promotion_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___PromotionFeedItem] = None,
        location_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___LocationFeedItem] = None,
        affiliate_location_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___AffiliateLocationFeedItem] = None,
        hotel_callout_feed_item : typing___Optional[google___ads___googleads___v2___common___extensions_pb2___HotelCalloutFeedItem] = None,
        targeted_campaign : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        targeted_ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ExtensionFeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"affiliate_location_feed_item",u"app_feed_item",u"call_feed_item",u"callout_feed_item",u"end_date_time",u"extension",u"hotel_callout_feed_item",u"id",u"location_feed_item",u"price_feed_item",u"promotion_feed_item",u"serving_resource_targeting",u"sitelink_feed_item",u"start_date_time",u"structured_snippet_feed_item",u"targeted_ad_group",u"targeted_campaign",u"targeted_geo_target_constant",u"targeted_keyword",u"text_message_feed_item"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_schedules",u"affiliate_location_feed_item",u"app_feed_item",u"call_feed_item",u"callout_feed_item",u"device",u"end_date_time",u"extension",u"extension_type",u"hotel_callout_feed_item",u"id",u"location_feed_item",u"price_feed_item",u"promotion_feed_item",u"resource_name",u"serving_resource_targeting",u"sitelink_feed_item",u"start_date_time",u"status",u"structured_snippet_feed_item",u"targeted_ad_group",u"targeted_campaign",u"targeted_geo_target_constant",u"targeted_keyword",u"text_message_feed_item"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"affiliate_location_feed_item",b"affiliate_location_feed_item",u"app_feed_item",b"app_feed_item",u"call_feed_item",b"call_feed_item",u"callout_feed_item",b"callout_feed_item",u"end_date_time",b"end_date_time",u"extension",b"extension",u"hotel_callout_feed_item",b"hotel_callout_feed_item",u"id",b"id",u"location_feed_item",b"location_feed_item",u"price_feed_item",b"price_feed_item",u"promotion_feed_item",b"promotion_feed_item",u"serving_resource_targeting",b"serving_resource_targeting",u"sitelink_feed_item",b"sitelink_feed_item",u"start_date_time",b"start_date_time",u"structured_snippet_feed_item",b"structured_snippet_feed_item",u"targeted_ad_group",b"targeted_ad_group",u"targeted_campaign",b"targeted_campaign",u"targeted_geo_target_constant",b"targeted_geo_target_constant",u"targeted_keyword",b"targeted_keyword",u"text_message_feed_item",b"text_message_feed_item"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_schedules",b"ad_schedules",u"affiliate_location_feed_item",b"affiliate_location_feed_item",u"app_feed_item",b"app_feed_item",u"call_feed_item",b"call_feed_item",u"callout_feed_item",b"callout_feed_item",u"device",b"device",u"end_date_time",b"end_date_time",u"extension",b"extension",u"extension_type",b"extension_type",u"hotel_callout_feed_item",b"hotel_callout_feed_item",u"id",b"id",u"location_feed_item",b"location_feed_item",u"price_feed_item",b"price_feed_item",u"promotion_feed_item",b"promotion_feed_item",u"resource_name",b"resource_name",u"serving_resource_targeting",b"serving_resource_targeting",u"sitelink_feed_item",b"sitelink_feed_item",u"start_date_time",b"start_date_time",u"status",b"status",u"structured_snippet_feed_item",b"structured_snippet_feed_item",u"targeted_ad_group",b"targeted_ad_group",u"targeted_campaign",b"targeted_campaign",u"targeted_geo_target_constant",b"targeted_geo_target_constant",u"targeted_keyword",b"targeted_keyword",u"text_message_feed_item",b"text_message_feed_item"]) -> None: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"extension",b"extension"]) -> typing_extensions___Literal["sitelink_feed_item","structured_snippet_feed_item","app_feed_item","call_feed_item","callout_feed_item","text_message_feed_item","price_feed_item","promotion_feed_item","location_feed_item","affiliate_location_feed_item","hotel_callout_feed_item"]: ...
    @typing___overload
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"serving_resource_targeting",b"serving_resource_targeting"]) -> typing_extensions___Literal["targeted_campaign","targeted_ad_group"]: ...

# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.common.criteria_pb2 import (
    DeviceInfo as google___ads___googleads___v3___common___criteria_pb2___DeviceInfo,
    HotelAdvanceBookingWindowInfo as google___ads___googleads___v3___common___criteria_pb2___HotelAdvanceBookingWindowInfo,
    HotelCheckInDayInfo as google___ads___googleads___v3___common___criteria_pb2___HotelCheckInDayInfo,
    HotelDateSelectionTypeInfo as google___ads___googleads___v3___common___criteria_pb2___HotelDateSelectionTypeInfo,
    HotelLengthOfStayInfo as google___ads___googleads___v3___common___criteria_pb2___HotelLengthOfStayInfo,
    PreferredContentInfo as google___ads___googleads___v3___common___criteria_pb2___PreferredContentInfo,
)

from google.ads.google_ads.v3.proto.enums.bid_modifier_source_pb2 import (
    BidModifierSourceEnum as google___ads___googleads___v3___enums___bid_modifier_source_pb2___BidModifierSourceEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class AdGroupBidModifier(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    bid_modifier_source = (
        ...
    )  # type: google___ads___googleads___v3___enums___bid_modifier_source_pb2___BidModifierSourceEnum.BidModifierSource
    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def base_ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hotel_date_selection_type(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___HotelDateSelectionTypeInfo: ...
    @property
    def hotel_advance_booking_window(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___HotelAdvanceBookingWindowInfo: ...
    @property
    def hotel_length_of_stay(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___HotelLengthOfStayInfo: ...
    @property
    def hotel_check_in_day(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___HotelCheckInDayInfo: ...
    @property
    def device(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___DeviceInfo: ...
    @property
    def preferred_content(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___PreferredContentInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        base_ad_group: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        bid_modifier_source: typing___Optional[
            google___ads___googleads___v3___enums___bid_modifier_source_pb2___BidModifierSourceEnum.BidModifierSource
        ] = None,
        hotel_date_selection_type: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___HotelDateSelectionTypeInfo
        ] = None,
        hotel_advance_booking_window: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___HotelAdvanceBookingWindowInfo
        ] = None,
        hotel_length_of_stay: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___HotelLengthOfStayInfo
        ] = None,
        hotel_check_in_day: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___HotelCheckInDayInfo
        ] = None,
        device: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___DeviceInfo
        ] = None,
        preferred_content: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___PreferredContentInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupBidModifier: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AdGroupBidModifier: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group",
            b"ad_group",
            "base_ad_group",
            b"base_ad_group",
            "bid_modifier",
            b"bid_modifier",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "device",
            b"device",
            "hotel_advance_booking_window",
            b"hotel_advance_booking_window",
            "hotel_check_in_day",
            b"hotel_check_in_day",
            "hotel_date_selection_type",
            b"hotel_date_selection_type",
            "hotel_length_of_stay",
            b"hotel_length_of_stay",
            "preferred_content",
            b"preferred_content",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group",
            b"ad_group",
            "base_ad_group",
            b"base_ad_group",
            "bid_modifier",
            b"bid_modifier",
            "bid_modifier_source",
            b"bid_modifier_source",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "device",
            b"device",
            "hotel_advance_booking_window",
            b"hotel_advance_booking_window",
            "hotel_check_in_day",
            b"hotel_check_in_day",
            "hotel_date_selection_type",
            b"hotel_date_selection_type",
            "hotel_length_of_stay",
            b"hotel_length_of_stay",
            "preferred_content",
            b"preferred_content",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["criterion", b"criterion"]
    ) -> typing_extensions___Literal[
        "hotel_date_selection_type",
        "hotel_advance_booking_window",
        "hotel_length_of_stay",
        "hotel_check_in_day",
        "device",
        "preferred_content",
    ]: ...

global___AdGroupBidModifier = AdGroupBidModifier

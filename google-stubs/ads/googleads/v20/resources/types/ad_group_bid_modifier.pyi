from google.ads.googleads.v20.common.types.criteria import HotelCheckInDateRangeInfo
from google.ads.googleads.v20.common.types.criteria import DeviceInfo
from google.ads.googleads.v20.common.types.criteria import HotelCheckInDayInfo
from google.ads.googleads.v20.common.types.criteria import HotelLengthOfStayInfo
from google.ads.googleads.v20.common.types.criteria import HotelAdvanceBookingWindowInfo
from google.ads.googleads.v20.common.types.criteria import HotelDateSelectionTypeInfo
from google.ads.googleads.v20.enums.types.bid_modifier_source import BidModifierSourceEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupBidModifier(proto.Message):
    resource_name: str
    ad_group: str
    criterion_id: int
    bid_modifier: float
    base_ad_group: str
    bid_modifier_source: BidModifierSourceEnum.BidModifierSource
    hotel_date_selection_type: HotelDateSelectionTypeInfo
    hotel_advance_booking_window: HotelAdvanceBookingWindowInfo
    hotel_length_of_stay: HotelLengthOfStayInfo
    hotel_check_in_day: HotelCheckInDayInfo
    device: DeviceInfo
    hotel_check_in_date_range: HotelCheckInDateRangeInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., ad_group: str = ..., criterion_id: int = ..., bid_modifier: float = ..., base_ad_group: str = ..., bid_modifier_source: BidModifierSourceEnum.BidModifierSource = ..., hotel_date_selection_type: HotelDateSelectionTypeInfo = ..., hotel_advance_booking_window: HotelAdvanceBookingWindowInfo = ..., hotel_length_of_stay: HotelLengthOfStayInfo = ..., hotel_check_in_day: HotelCheckInDayInfo = ..., device: DeviceInfo = ..., hotel_check_in_date_range: HotelCheckInDateRangeInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group", "criterion_id", "bid_modifier", "base_ad_group", "bid_modifier_source", "hotel_date_selection_type", "hotel_advance_booking_window", "hotel_length_of_stay", "hotel_check_in_day", "device", "hotel_check_in_date_range"]) -> bool: ...

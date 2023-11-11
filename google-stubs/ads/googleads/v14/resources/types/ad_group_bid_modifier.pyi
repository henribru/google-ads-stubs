from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.criteria import (
    DeviceInfo,
    HotelAdvanceBookingWindowInfo,
    HotelCheckInDateRangeInfo,
    HotelCheckInDayInfo,
    HotelDateSelectionTypeInfo,
    HotelLengthOfStayInfo,
)
from google.ads.googleads.v14.enums.types.bid_modifier_source import (
    BidModifierSourceEnum,
)

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group: str = ...,
        criterion_id: int = ...,
        bid_modifier: float = ...,
        base_ad_group: str = ...,
        bid_modifier_source: BidModifierSourceEnum.BidModifierSource = ...,
        hotel_date_selection_type: HotelDateSelectionTypeInfo = ...,
        hotel_advance_booking_window: HotelAdvanceBookingWindowInfo = ...,
        hotel_length_of_stay: HotelLengthOfStayInfo = ...,
        hotel_check_in_day: HotelCheckInDayInfo = ...,
        device: DeviceInfo = ...,
        hotel_check_in_date_range: HotelCheckInDateRangeInfo = ...
    ) -> None: ...

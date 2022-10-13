from typing import Any

import proto

from google.ads.googleads.v10.common.types.criteria import (
    DeviceInfo,
    HotelAdvanceBookingWindowInfo,
    HotelCheckInDateRangeInfo,
    HotelCheckInDayInfo,
    HotelDateSelectionTypeInfo,
    HotelLengthOfStayInfo,
    PreferredContentInfo,
)
from google.ads.googleads.v10.enums.types.bid_modifier_source import (
    BidModifierSourceEnum,
)

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
    preferred_content: PreferredContentInfo
    hotel_check_in_date_range: HotelCheckInDateRangeInfo
    def __init__(
        self,
        mapping: Any | None = ...,
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
        preferred_content: PreferredContentInfo = ...,
        hotel_check_in_date_range: HotelCheckInDateRangeInfo = ...
    ) -> None: ...

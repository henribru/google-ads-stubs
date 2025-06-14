import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import criteria
from google.ads.googleads.v19.enums.types import bid_modifier_source as gage_bid_modifier_source

__protobuf__: Incomplete

class AdGroupBidModifier(proto.Message):
    resource_name: str
    ad_group: str
    criterion_id: int
    bid_modifier: float
    base_ad_group: str
    bid_modifier_source: gage_bid_modifier_source.BidModifierSourceEnum.BidModifierSource
    hotel_date_selection_type: criteria.HotelDateSelectionTypeInfo
    hotel_advance_booking_window: criteria.HotelAdvanceBookingWindowInfo
    hotel_length_of_stay: criteria.HotelLengthOfStayInfo
    hotel_check_in_day: criteria.HotelCheckInDayInfo
    device: criteria.DeviceInfo
    hotel_check_in_date_range: criteria.HotelCheckInDateRangeInfo

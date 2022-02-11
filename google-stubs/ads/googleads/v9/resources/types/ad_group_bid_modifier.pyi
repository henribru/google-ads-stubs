from typing import Any

import proto

from google.ads.googleads.v9.common.types import criteria as criteria

__protobuf__: Any

class AdGroupBidModifier(proto.Message):
    resource_name: Any
    ad_group: Any
    criterion_id: Any
    bid_modifier: Any
    base_ad_group: Any
    bid_modifier_source: Any
    hotel_date_selection_type: Any
    hotel_advance_booking_window: Any
    hotel_length_of_stay: Any
    hotel_check_in_day: Any
    device: Any
    preferred_content: Any
    hotel_check_in_date_range: Any

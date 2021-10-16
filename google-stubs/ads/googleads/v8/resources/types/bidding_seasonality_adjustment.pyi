from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    advertising_channel_type as advertising_channel_type,
    device as device,
    seasonality_event_scope as seasonality_event_scope,
    seasonality_event_status as seasonality_event_status,
)

__protobuf__: Any

class BiddingSeasonalityAdjustment(proto.Message):
    resource_name: Any
    seasonality_adjustment_id: Any
    scope: Any
    status: Any
    start_date_time: Any
    end_date_time: Any
    name: Any
    description: Any
    devices: Any
    conversion_rate_modifier: Any
    campaigns: Any
    advertising_channel_types: Any

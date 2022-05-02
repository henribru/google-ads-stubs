import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    advertising_channel_type as advertising_channel_type,
    device as device,
    seasonality_event_scope as seasonality_event_scope,
    seasonality_event_status as seasonality_event_status,
)

__protobuf__: Incomplete

class BiddingSeasonalityAdjustment(proto.Message):
    resource_name: Incomplete
    seasonality_adjustment_id: Incomplete
    scope: Incomplete
    status: Incomplete
    start_date_time: Incomplete
    end_date_time: Incomplete
    name: Incomplete
    description: Incomplete
    devices: Incomplete
    conversion_rate_modifier: Incomplete
    campaigns: Incomplete
    advertising_channel_types: Incomplete

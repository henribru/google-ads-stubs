import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import advertising_channel_type, device, seasonality_event_scope, seasonality_event_status
from typing import MutableSequence

__protobuf__: Incomplete

class BiddingSeasonalityAdjustment(proto.Message):
    resource_name: str
    seasonality_adjustment_id: int
    scope: seasonality_event_scope.SeasonalityEventScopeEnum.SeasonalityEventScope
    status: seasonality_event_status.SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: MutableSequence[device.DeviceEnum.Device]
    conversion_rate_modifier: float
    campaigns: MutableSequence[str]
    advertising_channel_types: MutableSequence[advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType]

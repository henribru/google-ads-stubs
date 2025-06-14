import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import advertising_channel_type, device, seasonality_event_scope, seasonality_event_status
from typing import MutableSequence

__protobuf__: Incomplete

class BiddingDataExclusion(proto.Message):
    resource_name: str
    data_exclusion_id: int
    scope: seasonality_event_scope.SeasonalityEventScopeEnum.SeasonalityEventScope
    status: seasonality_event_status.SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: MutableSequence[device.DeviceEnum.Device]
    campaigns: MutableSequence[str]
    advertising_channel_types: MutableSequence[advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType]

from typing import Any

import proto

from google.ads.googleads.v11.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v11.enums.types.device import DeviceEnum
from google.ads.googleads.v11.enums.types.seasonality_event_scope import (
    SeasonalityEventScopeEnum,
)
from google.ads.googleads.v11.enums.types.seasonality_event_status import (
    SeasonalityEventStatusEnum,
)

class BiddingSeasonalityAdjustment(proto.Message):
    resource_name: str
    seasonality_adjustment_id: int
    scope: SeasonalityEventScopeEnum.SeasonalityEventScope
    status: SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: list[DeviceEnum.Device]
    conversion_rate_modifier: float
    campaigns: list[str]
    advertising_channel_types: list[AdvertisingChannelTypeEnum.AdvertisingChannelType]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        seasonality_adjustment_id: int = ...,
        scope: SeasonalityEventScopeEnum.SeasonalityEventScope = ...,
        status: SeasonalityEventStatusEnum.SeasonalityEventStatus = ...,
        start_date_time: str = ...,
        end_date_time: str = ...,
        name: str = ...,
        description: str = ...,
        devices: list[DeviceEnum.Device] = ...,
        conversion_rate_modifier: float = ...,
        campaigns: list[str] = ...,
        advertising_channel_types: list[
            AdvertisingChannelTypeEnum.AdvertisingChannelType
        ] = ...
    ) -> None: ...

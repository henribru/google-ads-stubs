from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v13.enums.types.device import DeviceEnum
from google.ads.googleads.v13.enums.types.seasonality_event_scope import (
    SeasonalityEventScopeEnum,
)
from google.ads.googleads.v13.enums.types.seasonality_event_status import (
    SeasonalityEventStatusEnum,
)

_M = TypeVar("_M")

class BiddingSeasonalityAdjustment(proto.Message):
    resource_name: str
    seasonality_adjustment_id: int
    scope: SeasonalityEventScopeEnum.SeasonalityEventScope
    status: SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: MutableSequence[DeviceEnum.Device]
    conversion_rate_modifier: float
    campaigns: MutableSequence[str]
    advertising_channel_types: MutableSequence[
        AdvertisingChannelTypeEnum.AdvertisingChannelType
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        seasonality_adjustment_id: int = ...,
        scope: SeasonalityEventScopeEnum.SeasonalityEventScope = ...,
        status: SeasonalityEventStatusEnum.SeasonalityEventStatus = ...,
        start_date_time: str = ...,
        end_date_time: str = ...,
        name: str = ...,
        description: str = ...,
        devices: MutableSequence[DeviceEnum.Device] = ...,
        conversion_rate_modifier: float = ...,
        campaigns: MutableSequence[str] = ...,
        advertising_channel_types: MutableSequence[
            AdvertisingChannelTypeEnum.AdvertisingChannelType
        ] = ...
    ) -> None: ...

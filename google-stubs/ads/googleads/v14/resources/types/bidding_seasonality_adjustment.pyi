from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v14.enums.types.device import DeviceEnum
from google.ads.googleads.v14.enums.types.seasonality_event_scope import (
    SeasonalityEventScopeEnum,
)
from google.ads.googleads.v14.enums.types.seasonality_event_status import (
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
    def __contains__(self, key: Literal["resource_name", "seasonality_adjustment_id", "scope", "status", "start_date_time", "end_date_time", "name", "description", "devices", "conversion_rate_modifier", "campaigns", "advertising_channel_types"]) -> bool: ...  # type: ignore[override]

from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.advertising_channel_type import AdvertisingChannelTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.device import DeviceEnum
from google.ads.googleads.v19.enums.types.seasonality_event_status import SeasonalityEventStatusEnum
from google.ads.googleads.v19.enums.types.seasonality_event_scope import SeasonalityEventScopeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BiddingDataExclusion(proto.Message):
    resource_name: str
    data_exclusion_id: int
    scope: SeasonalityEventScopeEnum.SeasonalityEventScope
    status: SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: MutableSequence[DeviceEnum.Device]
    campaigns: MutableSequence[str]
    advertising_channel_types: MutableSequence[AdvertisingChannelTypeEnum.AdvertisingChannelType]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., data_exclusion_id: int = ..., scope: SeasonalityEventScopeEnum.SeasonalityEventScope = ..., status: SeasonalityEventStatusEnum.SeasonalityEventStatus = ..., start_date_time: str = ..., end_date_time: str = ..., name: str = ..., description: str = ..., devices: MutableSequence[DeviceEnum.Device] = ..., campaigns: MutableSequence[str] = ..., advertising_channel_types: MutableSequence[AdvertisingChannelTypeEnum.AdvertisingChannelType] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "data_exclusion_id", "scope", "status", "start_date_time", "end_date_time", "name", "description", "devices", "campaigns", "advertising_channel_types"]) -> bool: ...

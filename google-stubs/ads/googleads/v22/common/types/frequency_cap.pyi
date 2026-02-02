from google.ads.googleads.v22.enums.types.frequency_cap_time_unit import FrequencyCapTimeUnitEnum
from google.ads.googleads.v22.enums.types.frequency_cap_event_type import FrequencyCapEventTypeEnum
from google.ads.googleads.v22.enums.types.frequency_cap_level import FrequencyCapLevelEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FrequencyCapEntry(proto.Message):
    key: FrequencyCapKey
    cap: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, key: FrequencyCapKey = ..., cap: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["key", "cap"]) -> bool: ...
class FrequencyCapKey(proto.Message):
    level: FrequencyCapLevelEnum.FrequencyCapLevel
    event_type: FrequencyCapEventTypeEnum.FrequencyCapEventType
    time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    time_length: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, level: FrequencyCapLevelEnum.FrequencyCapLevel = ..., event_type: FrequencyCapEventTypeEnum.FrequencyCapEventType = ..., time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit = ..., time_length: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["level", "event_type", "time_unit", "time_length"]) -> bool: ...

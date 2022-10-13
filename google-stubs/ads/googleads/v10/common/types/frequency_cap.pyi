from typing import Any

import proto

from google.ads.googleads.v10.enums.types.frequency_cap_event_type import (
    FrequencyCapEventTypeEnum,
)
from google.ads.googleads.v10.enums.types.frequency_cap_level import (
    FrequencyCapLevelEnum,
)
from google.ads.googleads.v10.enums.types.frequency_cap_time_unit import (
    FrequencyCapTimeUnitEnum,
)

class FrequencyCapEntry(proto.Message):
    key: FrequencyCapKey
    cap: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        key: FrequencyCapKey = ...,
        cap: int = ...
    ) -> None: ...

class FrequencyCapKey(proto.Message):
    level: FrequencyCapLevelEnum.FrequencyCapLevel
    event_type: FrequencyCapEventTypeEnum.FrequencyCapEventType
    time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    time_length: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        level: FrequencyCapLevelEnum.FrequencyCapLevel = ...,
        event_type: FrequencyCapEventTypeEnum.FrequencyCapEventType = ...,
        time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit = ...,
        time_length: int = ...
    ) -> None: ...

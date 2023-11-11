from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.frequency_cap_event_type import (
    FrequencyCapEventTypeEnum,
)
from google.ads.googleads.v13.enums.types.frequency_cap_level import (
    FrequencyCapLevelEnum,
)
from google.ads.googleads.v13.enums.types.frequency_cap_time_unit import (
    FrequencyCapTimeUnitEnum,
)

_M = TypeVar("_M")

class FrequencyCapEntry(proto.Message):
    key: FrequencyCapKey
    cap: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        level: FrequencyCapLevelEnum.FrequencyCapLevel = ...,
        event_type: FrequencyCapEventTypeEnum.FrequencyCapEventType = ...,
        time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit = ...,
        time_length: int = ...
    ) -> None: ...

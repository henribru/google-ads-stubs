from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    frequency_cap_event_type as frequency_cap_event_type,
    frequency_cap_level as frequency_cap_level,
    frequency_cap_time_unit as frequency_cap_time_unit,
)

__protobuf__: Any

class FrequencyCapEntry(proto.Message):
    key: Any
    cap: Any

class FrequencyCapKey(proto.Message):
    level: Any
    event_type: Any
    time_unit: Any
    time_length: Any

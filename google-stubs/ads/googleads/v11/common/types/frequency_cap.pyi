import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    frequency_cap_event_type as frequency_cap_event_type,
    frequency_cap_level as frequency_cap_level,
    frequency_cap_time_unit as frequency_cap_time_unit,
)

__protobuf__: Incomplete

class FrequencyCapEntry(proto.Message):
    key: Incomplete
    cap: Incomplete

class FrequencyCapKey(proto.Message):
    level: Incomplete
    event_type: Incomplete
    time_unit: Incomplete
    time_length: Incomplete

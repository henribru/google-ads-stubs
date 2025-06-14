import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import frequency_cap_event_type, frequency_cap_level, frequency_cap_time_unit

__protobuf__: Incomplete

class FrequencyCapEntry(proto.Message):
    key: FrequencyCapKey
    cap: int

class FrequencyCapKey(proto.Message):
    level: frequency_cap_level.FrequencyCapLevelEnum.FrequencyCapLevel
    event_type: frequency_cap_event_type.FrequencyCapEventTypeEnum.FrequencyCapEventType
    time_unit: frequency_cap_time_unit.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    time_length: int

from typing import Any

import proto

__protobuf__: Any

class OfflineUserDataJobMatchRateRangeEnum(proto.Message):
    class OfflineUserDataJobMatchRateRange(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MATCH_RANGE_LESS_THAN_20: int
        MATCH_RANGE_20_TO_30: int
        MATCH_RANGE_31_TO_40: int
        MATCH_RANGE_41_TO_50: int
        MATCH_RANGE_51_TO_60: int
        MATCH_RANGE_61_TO_70: int
        MATCH_RANGE_71_TO_80: int
        MATCH_RANGE_81_TO_90: int
        MATCH_RANGE_91_TO_100: int

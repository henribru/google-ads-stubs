from typing import Any

import proto

__protobuf__: Any

class AgeRangeTypeEnum(proto.Message):
    class AgeRangeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AGE_RANGE_18_24: int
        AGE_RANGE_25_34: int
        AGE_RANGE_35_44: int
        AGE_RANGE_45_54: int
        AGE_RANGE_55_64: int
        AGE_RANGE_65_UP: int
        AGE_RANGE_UNDETERMINED: int

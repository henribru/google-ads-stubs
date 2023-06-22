from typing import Any

import proto

class AgeRangeTypeEnum(proto.Message):
    class AgeRangeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AGE_RANGE_18_24 = 503001
        AGE_RANGE_25_34 = 503002
        AGE_RANGE_35_44 = 503003
        AGE_RANGE_45_54 = 503004
        AGE_RANGE_55_64 = 503005
        AGE_RANGE_65_UP = 503006
        AGE_RANGE_UNDETERMINED = 503999
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

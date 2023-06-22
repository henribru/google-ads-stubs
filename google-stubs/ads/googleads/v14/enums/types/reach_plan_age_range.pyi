from typing import Any

import proto

class ReachPlanAgeRangeEnum(proto.Message):
    class ReachPlanAgeRange(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AGE_RANGE_18_24 = 503001
        AGE_RANGE_18_34 = 2
        AGE_RANGE_18_44 = 3
        AGE_RANGE_18_49 = 4
        AGE_RANGE_18_54 = 5
        AGE_RANGE_18_64 = 6
        AGE_RANGE_18_65_UP = 7
        AGE_RANGE_21_34 = 8
        AGE_RANGE_25_34 = 503002
        AGE_RANGE_25_44 = 9
        AGE_RANGE_25_49 = 10
        AGE_RANGE_25_54 = 11
        AGE_RANGE_25_64 = 12
        AGE_RANGE_25_65_UP = 13
        AGE_RANGE_35_44 = 503003
        AGE_RANGE_35_49 = 14
        AGE_RANGE_35_54 = 15
        AGE_RANGE_35_64 = 16
        AGE_RANGE_35_65_UP = 17
        AGE_RANGE_45_54 = 503004
        AGE_RANGE_45_64 = 18
        AGE_RANGE_45_65_UP = 19
        AGE_RANGE_50_65_UP = 20
        AGE_RANGE_55_64 = 503005
        AGE_RANGE_55_65_UP = 21
        AGE_RANGE_65_UP = 503006
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class DistanceBucketEnum(proto.Message):
    class DistanceBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WITHIN_700M = 2
        WITHIN_1KM = 3
        WITHIN_5KM = 4
        WITHIN_10KM = 5
        WITHIN_15KM = 6
        WITHIN_20KM = 7
        WITHIN_25KM = 8
        WITHIN_30KM = 9
        WITHIN_35KM = 10
        WITHIN_40KM = 11
        WITHIN_45KM = 12
        WITHIN_50KM = 13
        WITHIN_55KM = 14
        WITHIN_60KM = 15
        WITHIN_65KM = 16
        BEYOND_65KM = 17
        WITHIN_0_7MILES = 18
        WITHIN_1MILE = 19
        WITHIN_5MILES = 20
        WITHIN_10MILES = 21
        WITHIN_15MILES = 22
        WITHIN_20MILES = 23
        WITHIN_25MILES = 24
        WITHIN_30MILES = 25
        WITHIN_35MILES = 26
        WITHIN_40MILES = 27
        BEYOND_40MILES = 28
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

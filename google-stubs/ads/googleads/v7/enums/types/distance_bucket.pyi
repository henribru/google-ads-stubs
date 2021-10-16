from typing import Any

import proto

__protobuf__: Any

class DistanceBucketEnum(proto.Message):
    class DistanceBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WITHIN_700M: int
        WITHIN_1KM: int
        WITHIN_5KM: int
        WITHIN_10KM: int
        WITHIN_15KM: int
        WITHIN_20KM: int
        WITHIN_25KM: int
        WITHIN_30KM: int
        WITHIN_35KM: int
        WITHIN_40KM: int
        WITHIN_45KM: int
        WITHIN_50KM: int
        WITHIN_55KM: int
        WITHIN_60KM: int
        WITHIN_65KM: int
        BEYOND_65KM: int
        WITHIN_0_7MILES: int
        WITHIN_1MILE: int
        WITHIN_5MILES: int
        WITHIN_10MILES: int
        WITHIN_15MILES: int
        WITHIN_20MILES: int
        WITHIN_25MILES: int
        WITHIN_30MILES: int
        WITHIN_35MILES: int
        WITHIN_40MILES: int
        BEYOND_40MILES: int

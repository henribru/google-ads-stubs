from typing import Any

import proto

__protobuf__: Any

class QualityScoreBucketEnum(proto.Message):
    class QualityScoreBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BELOW_AVERAGE: int
        AVERAGE: int
        ABOVE_AVERAGE: int

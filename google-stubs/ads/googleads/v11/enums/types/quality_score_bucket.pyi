from typing import Any

import proto

class QualityScoreBucketEnum(proto.Message):
    class QualityScoreBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BELOW_AVERAGE = 2
        AVERAGE = 3
        ABOVE_AVERAGE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

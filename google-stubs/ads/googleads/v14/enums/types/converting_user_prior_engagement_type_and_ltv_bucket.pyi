from typing import Any

import proto

class ConvertingUserPriorEngagementTypeAndLtvBucketEnum(proto.Message):
    class ConvertingUserPriorEngagementTypeAndLtvBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 2
        RETURNING = 3
        NEW_AND_HIGH_LTV = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

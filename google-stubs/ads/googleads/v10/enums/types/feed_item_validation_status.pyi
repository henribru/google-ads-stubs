from typing import Any

import proto

class FeedItemValidationStatusEnum(proto.Message):
    class FeedItemValidationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING = 2
        INVALID = 3
        VALID = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

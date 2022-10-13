from typing import Any

import proto

class PartialFailureErrorEnum(proto.Message):
    class PartialFailureError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PARTIAL_FAILURE_MODE_REQUIRED = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

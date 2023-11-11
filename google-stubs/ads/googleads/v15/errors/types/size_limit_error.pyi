from typing import Any

import proto

class SizeLimitErrorEnum(proto.Message):
    class SizeLimitError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUEST_SIZE_LIMIT_EXCEEDED = 2
        RESPONSE_SIZE_LIMIT_EXCEEDED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class ResourceAccessDeniedErrorEnum(proto.Message):
    class ResourceAccessDeniedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WRITE_ACCESS_DENIED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

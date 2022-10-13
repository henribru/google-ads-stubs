from typing import Any

import proto

class AdxErrorEnum(proto.Message):
    class AdxError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNSUPPORTED_FEATURE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

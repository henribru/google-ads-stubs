from typing import Any

import proto

class CallTypeEnum(proto.Message):
    class CallType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MANUALLY_DIALED = 2
        HIGH_END_MOBILE_SEARCH = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

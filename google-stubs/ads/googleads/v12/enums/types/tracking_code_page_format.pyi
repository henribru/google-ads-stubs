from typing import Any

import proto

class TrackingCodePageFormatEnum(proto.Message):
    class TrackingCodePageFormat(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HTML = 2
        AMP = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class OfflineConversionDiagnosticStatusEnum(proto.Message):
    class OfflineConversionDiagnosticStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXCELLENT = 2
        GOOD = 3
        NEEDS_ATTENTION = 4
        NO_RECENT_UPLOAD = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class AdGroupAdRotationModeEnum(proto.Message):
    class AdGroupAdRotationMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTIMIZE = 2
        ROTATE_FOREVER = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

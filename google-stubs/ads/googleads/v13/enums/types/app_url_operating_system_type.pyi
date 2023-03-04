from typing import Any

import proto

class AppUrlOperatingSystemTypeEnum(proto.Message):
    class AppUrlOperatingSystemType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IOS = 2
        ANDROID = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

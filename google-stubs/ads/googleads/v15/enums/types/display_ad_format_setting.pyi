from typing import Any

import proto

class DisplayAdFormatSettingEnum(proto.Message):
    class DisplayAdFormatSetting(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_FORMATS = 2
        NON_NATIVE = 3
        NATIVE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

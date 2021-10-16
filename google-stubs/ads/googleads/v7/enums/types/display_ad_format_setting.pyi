from typing import Any

import proto

__protobuf__: Any

class DisplayAdFormatSettingEnum(proto.Message):
    class DisplayAdFormatSetting(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ALL_FORMATS: int
        NON_NATIVE: int
        NATIVE: int

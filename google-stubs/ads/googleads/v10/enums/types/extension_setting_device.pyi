from typing import Any

import proto

class ExtensionSettingDeviceEnum(proto.Message):
    class ExtensionSettingDevice(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MOBILE = 2
        DESKTOP = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

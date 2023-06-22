from typing import Any

import proto

class DeviceEnum(proto.Message):
    class Device(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MOBILE = 2
        TABLET = 3
        DESKTOP = 4
        CONNECTED_TV = 6
        OTHER = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

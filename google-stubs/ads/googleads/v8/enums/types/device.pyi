from typing import Any

import proto

__protobuf__: Any

class DeviceEnum(proto.Message):
    class Device(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MOBILE: int
        TABLET: int
        DESKTOP: int
        CONNECTED_TV: int
        OTHER: int

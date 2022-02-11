from typing import Any

import proto

__protobuf__: Any

class AccessReasonEnum(proto.Message):
    class AccessReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OWNED: int
        SHARED: int
        LICENSED: int
        SUBSCRIBED: int
        AFFILIATED: int

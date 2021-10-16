from typing import Any

import proto

__protobuf__: Any

class ManagerLinkStatusEnum(proto.Message):
    class ManagerLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTIVE: int
        INACTIVE: int
        PENDING: int
        REFUSED: int
        CANCELED: int

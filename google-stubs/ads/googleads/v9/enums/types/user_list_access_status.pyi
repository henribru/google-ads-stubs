from typing import Any

import proto

__protobuf__: Any

class UserListAccessStatusEnum(proto.Message):
    class UserListAccessStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        DISABLED: int

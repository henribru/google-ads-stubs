from typing import Any

import proto

__protobuf__: Any

class UserListMembershipStatusEnum(proto.Message):
    class UserListMembershipStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPEN: int
        CLOSED: int

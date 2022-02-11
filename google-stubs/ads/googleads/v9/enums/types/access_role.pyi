from typing import Any

import proto

__protobuf__: Any

class AccessRoleEnum(proto.Message):
    class AccessRole(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADMIN: int
        STANDARD: int
        READ_ONLY: int
        EMAIL_ONLY: int

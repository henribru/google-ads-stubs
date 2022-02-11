from typing import Any

import proto

__protobuf__: Any

class UserIdentifierSourceEnum(proto.Message):
    class UserIdentifierSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FIRST_PARTY: int
        THIRD_PARTY: int

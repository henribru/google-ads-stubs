from typing import Any

import proto

__protobuf__: Any

class DatabaseErrorEnum(proto.Message):
    class DatabaseError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONCURRENT_MODIFICATION: int
        DATA_CONSTRAINT_VIOLATION: int
        REQUEST_TOO_LARGE: int

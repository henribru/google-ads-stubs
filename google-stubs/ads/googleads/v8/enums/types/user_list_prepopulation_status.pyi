from typing import Any

import proto

__protobuf__: Any

class UserListPrepopulationStatusEnum(proto.Message):
    class UserListPrepopulationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUESTED: int
        FINISHED: int
        FAILED: int

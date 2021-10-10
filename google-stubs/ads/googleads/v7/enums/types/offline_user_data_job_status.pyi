from typing import Any

import proto

__protobuf__: Any

class OfflineUserDataJobStatusEnum(proto.Message):
    class OfflineUserDataJobStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        RUNNING: int
        SUCCESS: int
        FAILED: int

from typing import Any

import proto

__protobuf__: Any

class BatchJobStatusEnum(proto.Message):
    class BatchJobStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        RUNNING: int
        DONE: int

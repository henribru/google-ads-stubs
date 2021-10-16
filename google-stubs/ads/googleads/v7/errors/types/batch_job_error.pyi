from typing import Any

import proto

__protobuf__: Any

class BatchJobErrorEnum(proto.Message):
    class BatchJobError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING: int
        EMPTY_OPERATIONS: int
        INVALID_SEQUENCE_TOKEN: int
        RESULTS_NOT_READY: int
        INVALID_PAGE_SIZE: int
        CAN_ONLY_REMOVE_PENDING_JOB: int

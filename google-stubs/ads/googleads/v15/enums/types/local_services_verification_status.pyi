from typing import Any

import proto

class LocalServicesVerificationStatusEnum(proto.Message):
    class LocalServicesVerificationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEEDS_REVIEW = 2
        FAILED = 3
        PASSED = 4
        NOT_APPLICABLE = 5
        NO_SUBMISSION = 6
        PARTIAL_SUBMISSION = 7
        PENDING_ESCALATION = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

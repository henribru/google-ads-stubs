from typing import Any

import proto

class LocalServicesVerificationArtifactStatusEnum(proto.Message):
    class LocalServicesVerificationArtifactStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PASSED = 2
        FAILED = 3
        PENDING = 4
        NO_SUBMISSION = 5
        CANCELLED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

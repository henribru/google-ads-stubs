from typing import Any

import proto

class PolicyViolationErrorEnum(proto.Message):
    class PolicyViolationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        POLICY_ERROR = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

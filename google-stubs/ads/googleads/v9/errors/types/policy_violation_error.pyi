from typing import Any

import proto

__protobuf__: Any

class PolicyViolationErrorEnum(proto.Message):
    class PolicyViolationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        POLICY_ERROR: int

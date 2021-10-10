from typing import Any

import proto

__protobuf__: Any

class PolicyFindingErrorEnum(proto.Message):
    class PolicyFindingError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        POLICY_FINDING: int
        POLICY_TOPIC_NOT_FOUND: int

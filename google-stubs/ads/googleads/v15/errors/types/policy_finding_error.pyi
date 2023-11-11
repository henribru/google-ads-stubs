from typing import Any

import proto

class PolicyFindingErrorEnum(proto.Message):
    class PolicyFindingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        POLICY_FINDING = 2
        POLICY_TOPIC_NOT_FOUND = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

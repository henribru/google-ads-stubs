from typing import Any

import proto

class PolicyValidationParameterErrorEnum(proto.Message):
    class PolicyValidationParameterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS = 2
        UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS = 3
        CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

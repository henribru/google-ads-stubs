from typing import Any

import proto

class ConversionValueRuleErrorEnum(proto.Message):
    class ConversionValueRuleError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_GEO_TARGET_CONSTANT = 2
        CONFLICTING_INCLUDED_AND_EXCLUDED_GEO_TARGET = 3
        CONFLICTING_CONDITIONS = 4
        CANNOT_REMOVE_IF_INCLUDED_IN_VALUE_RULE_SET = 5
        CONDITION_NOT_ALLOWED = 6
        FIELD_MUST_BE_UNSET = 7
        CANNOT_PAUSE_UNLESS_VALUE_RULE_SET_IS_PAUSED = 8
        UNTARGETABLE_GEO_TARGET = 9
        INVALID_AUDIENCE_USER_LIST = 10
        INACCESSIBLE_USER_LIST = 11
        INVALID_AUDIENCE_USER_INTEREST = 12
        CANNOT_ADD_RULE_WITH_STATUS_REMOVED = 13
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

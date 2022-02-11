from typing import Any

import proto

__protobuf__: Any

class ConversionValueRuleErrorEnum(proto.Message):
    class ConversionValueRuleError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_GEO_TARGET_CONSTANT: int
        CONFLICTING_INCLUDED_AND_EXCLUDED_GEO_TARGET: int
        CONFLICTING_CONDITIONS: int
        CANNOT_REMOVE_IF_INCLUDED_IN_VALUE_RULE_SET: int
        CONDITION_NOT_ALLOWED: int
        FIELD_MUST_BE_UNSET: int
        CANNOT_PAUSE_UNLESS_VALUE_RULE_SET_IS_PAUSED: int
        UNTARGETABLE_GEO_TARGET: int
        INVALID_AUDIENCE_USER_LIST: int
        INACCESSIBLE_USER_LIST: int
        INVALID_AUDIENCE_USER_INTEREST: int
        CANNOT_ADD_RULE_WITH_STATUS_REMOVED: int

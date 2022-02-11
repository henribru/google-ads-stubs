from typing import Any

import proto

__protobuf__: Any

class ConversionValueRuleSetErrorEnum(proto.Message):
    class ConversionValueRuleSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONFLICTING_VALUE_RULE_CONDITIONS: int
        INVALID_VALUE_RULE: int
        DIMENSIONS_UPDATE_ONLY_ALLOW_APPEND: int
        CONDITION_TYPE_NOT_ALLOWED: int
        DUPLICATE_DIMENSIONS: int
        INVALID_CAMPAIGN_ID: int
        CANNOT_PAUSE_UNLESS_ALL_VALUE_RULES_ARE_PAUSED: int
        SHOULD_PAUSE_WHEN_ALL_VALUE_RULES_ARE_PAUSED: int
        VALUE_RULES_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: int

from typing import Any

import proto

__protobuf__: Any

class RecommendationErrorEnum(proto.Message):
    class RecommendationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BUDGET_AMOUNT_TOO_SMALL: int
        BUDGET_AMOUNT_TOO_LARGE: int
        INVALID_BUDGET_AMOUNT: int
        POLICY_ERROR: int
        INVALID_BID_AMOUNT: int
        ADGROUP_KEYWORD_LIMIT: int
        RECOMMENDATION_ALREADY_APPLIED: int
        RECOMMENDATION_INVALIDATED: int
        TOO_MANY_OPERATIONS: int
        NO_OPERATIONS: int
        DIFFERENT_TYPES_NOT_SUPPORTED: int
        DUPLICATE_RESOURCE_NAME: int
        RECOMMENDATION_ALREADY_DISMISSED: int
        INVALID_APPLY_REQUEST: int

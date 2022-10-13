from typing import Any

import proto

class RecommendationErrorEnum(proto.Message):
    class RecommendationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUDGET_AMOUNT_TOO_SMALL = 2
        BUDGET_AMOUNT_TOO_LARGE = 3
        INVALID_BUDGET_AMOUNT = 4
        POLICY_ERROR = 5
        INVALID_BID_AMOUNT = 6
        ADGROUP_KEYWORD_LIMIT = 7
        RECOMMENDATION_ALREADY_APPLIED = 8
        RECOMMENDATION_INVALIDATED = 9
        TOO_MANY_OPERATIONS = 10
        NO_OPERATIONS = 11
        DIFFERENT_TYPES_NOT_SUPPORTED = 12
        DUPLICATE_RESOURCE_NAME = 13
        RECOMMENDATION_ALREADY_DISMISSED = 14
        INVALID_APPLY_REQUEST = 15
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

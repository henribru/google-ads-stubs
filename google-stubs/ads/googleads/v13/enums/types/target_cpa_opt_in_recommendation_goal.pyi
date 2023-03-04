from typing import Any

import proto

class TargetCpaOptInRecommendationGoalEnum(proto.Message):
    class TargetCpaOptInRecommendationGoal(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SAME_COST = 2
        SAME_CONVERSIONS = 3
        SAME_CPA = 4
        CLOSEST_CPA = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

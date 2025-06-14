import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class TargetCpaOptInRecommendationGoalEnum(proto.Message):
    class TargetCpaOptInRecommendationGoal(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SAME_COST: int
        SAME_CONVERSIONS: int
        SAME_CPA: int
        CLOSEST_CPA: int

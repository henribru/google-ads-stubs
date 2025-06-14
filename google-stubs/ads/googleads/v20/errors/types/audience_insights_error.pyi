import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AudienceInsightsErrorEnum(proto.Message):
    class AudienceInsightsError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS: int

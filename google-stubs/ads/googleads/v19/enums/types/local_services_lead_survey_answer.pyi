import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadSurveyAnswerEnum(proto.Message):
    class SurveyAnswer(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        VERY_SATISFIED: int
        SATISFIED: int
        NEUTRAL: int
        DISSATISFIED: int
        VERY_DISSATISFIED: int

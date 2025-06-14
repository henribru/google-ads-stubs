import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadSurveyDissatisfiedReasonEnum(proto.Message):
    class SurveyDissatisfiedReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OTHER_DISSATISFIED_REASON: int
        GEO_MISMATCH: int
        JOB_TYPE_MISMATCH: int
        NOT_READY_TO_BOOK: int
        SPAM: int
        DUPLICATE: int
        SOLICITATION: int

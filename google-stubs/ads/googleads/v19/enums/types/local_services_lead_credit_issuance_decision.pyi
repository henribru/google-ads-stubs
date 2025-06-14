import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadCreditIssuanceDecisionEnum(proto.Message):
    class CreditIssuanceDecision(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SUCCESS_NOT_REACHED_THRESHOLD: int
        SUCCESS_REACHED_THRESHOLD: int
        FAIL_OVER_THRESHOLD: int
        FAIL_NOT_ELIGIBLE: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadSurveySatisfiedReasonEnum(proto.Message):
    class SurveySatisfiedReason(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OTHER_SATISFIED_REASON: int
        BOOKED_CUSTOMER: int
        LIKELY_BOOKED_CUSTOMER: int
        SERVICE_RELATED: int
        HIGH_VALUE_SERVICE: int

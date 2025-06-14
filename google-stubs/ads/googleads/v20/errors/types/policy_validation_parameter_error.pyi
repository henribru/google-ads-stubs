import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PolicyValidationParameterErrorEnum(proto.Message):
    class PolicyValidationParameterError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS: int
        UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS: int
        CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS: int

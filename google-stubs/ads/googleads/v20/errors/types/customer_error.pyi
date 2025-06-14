import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerErrorEnum(proto.Message):
    class CustomerError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STATUS_CHANGE_DISALLOWED: int
        ACCOUNT_NOT_SET_UP: int
        CREATION_DENIED_FOR_POLICY_VIOLATION: int
        CREATION_DENIED_INELIGIBLE_MCC: int

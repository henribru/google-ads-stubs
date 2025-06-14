import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerLifecycleGoalErrorEnum(proto.Message):
    class CustomerLifecycleGoalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_ACQUISITION_VALUE_MISSING: int
        CUSTOMER_ACQUISITION_INVALID_VALUE: int
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE: int
        CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED: int
        CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED: int
        INVALID_EXISTING_USER_LIST: int
        INVALID_HIGH_LIFETIME_VALUE_USER_LIST: int

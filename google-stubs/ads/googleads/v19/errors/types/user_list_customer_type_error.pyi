import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListCustomerTypeErrorEnum(proto.Message):
    class UserListCustomerTypeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONFLICTING_CUSTOMER_TYPES: int
        NO_ACCESS_TO_USER_LIST: int
        USERLIST_NOT_ELIGIBLE: int
        CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT: int
        TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE: int

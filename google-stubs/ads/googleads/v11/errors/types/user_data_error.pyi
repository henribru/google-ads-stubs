import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserDataErrorEnum(proto.Message):
    class UserDataError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED: int
        TOO_MANY_USER_IDENTIFIERS: int
        USER_LIST_NOT_APPLICABLE: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class HeaderErrorEnum(proto.Message):
    class HeaderError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_LOGIN_CUSTOMER_ID: int
        INVALID_LINKED_CUSTOMER_ID: int

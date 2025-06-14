import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class OfflineUserDataJobTypeEnum(proto.Message):
    class OfflineUserDataJobType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        STORE_SALES_UPLOAD_FIRST_PARTY: int
        STORE_SALES_UPLOAD_THIRD_PARTY: int
        CUSTOMER_MATCH_USER_LIST: int
        CUSTOMER_MATCH_WITH_ATTRIBUTES: int

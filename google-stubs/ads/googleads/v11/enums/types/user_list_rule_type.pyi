import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListRuleTypeEnum(proto.Message):
    class UserListRuleType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AND_OF_ORS: int
        OR_OF_ANDS: int

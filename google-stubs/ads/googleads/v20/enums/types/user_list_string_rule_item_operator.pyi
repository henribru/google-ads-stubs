import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListStringRuleItemOperatorEnum(proto.Message):
    class UserListStringRuleItemOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONTAINS: int
        EQUALS: int
        STARTS_WITH: int
        ENDS_WITH: int
        NOT_EQUALS: int
        NOT_CONTAINS: int
        NOT_STARTS_WITH: int
        NOT_ENDS_WITH: int

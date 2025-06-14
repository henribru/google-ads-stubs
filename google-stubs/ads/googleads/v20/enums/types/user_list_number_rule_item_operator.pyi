import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListNumberRuleItemOperatorEnum(proto.Message):
    class UserListNumberRuleItemOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GREATER_THAN: int
        GREATER_THAN_OR_EQUAL: int
        EQUALS: int
        NOT_EQUALS: int
        LESS_THAN: int
        LESS_THAN_OR_EQUAL: int

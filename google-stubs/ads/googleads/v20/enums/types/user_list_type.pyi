import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListTypeEnum(proto.Message):
    class UserListType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REMARKETING: int
        LOGICAL: int
        EXTERNAL_REMARKETING: int
        RULE_BASED: int
        SIMILAR: int
        CRM_BASED: int
        LOOKALIKE: int

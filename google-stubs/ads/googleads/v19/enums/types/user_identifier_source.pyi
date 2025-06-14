import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserIdentifierSourceEnum(proto.Message):
    class UserIdentifierSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FIRST_PARTY: int
        THIRD_PARTY: int

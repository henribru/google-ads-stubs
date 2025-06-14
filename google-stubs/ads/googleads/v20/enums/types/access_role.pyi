import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AccessRoleEnum(proto.Message):
    class AccessRole(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADMIN: int
        STANDARD: int
        READ_ONLY: int
        EMAIL_ONLY: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesCreditStateEnum(proto.Message):
    class CreditState(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PENDING: int
        CREDITED: int

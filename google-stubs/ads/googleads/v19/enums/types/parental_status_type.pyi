import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ParentalStatusTypeEnum(proto.Message):
    class ParentalStatusType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PARENT: int
        NOT_A_PARENT: int
        UNDETERMINED: int

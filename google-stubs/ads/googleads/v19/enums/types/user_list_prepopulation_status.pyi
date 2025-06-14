import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListPrepopulationStatusEnum(proto.Message):
    class UserListPrepopulationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUESTED: int
        FINISHED: int
        FAILED: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExperimentStatusEnum(proto.Message):
    class ExperimentStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        HALTED: int
        PROMOTED: int
        SETUP: int
        INITIATED: int
        GRADUATED: int

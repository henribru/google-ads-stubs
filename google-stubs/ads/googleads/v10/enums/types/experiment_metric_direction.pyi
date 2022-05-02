import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExperimentMetricDirectionEnum(proto.Message):
    class ExperimentMetricDirection(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_CHANGE: int
        INCREASE: int
        DECREASE: int
        NO_CHANGE_OR_INCREASE: int
        NO_CHANGE_OR_DECREASE: int

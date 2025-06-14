import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ReachPlanErrorEnum(proto.Message):
    class ReachPlanError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_FORECASTABLE_MISSING_RATE: int
        NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY: int
        NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED: int

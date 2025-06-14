import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ClickViewErrorEnum(proto.Message):
    class ClickViewError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXPECTED_FILTER_ON_A_SINGLE_DAY: int
        DATE_TOO_OLD: int

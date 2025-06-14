import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CurrencyErrorEnum(proto.Message):
    class CurrencyError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT: int

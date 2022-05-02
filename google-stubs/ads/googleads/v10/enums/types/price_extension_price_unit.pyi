import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PriceExtensionPriceUnitEnum(proto.Message):
    class PriceExtensionPriceUnit(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PER_HOUR: int
        PER_DAY: int
        PER_WEEK: int
        PER_MONTH: int
        PER_YEAR: int
        PER_NIGHT: int

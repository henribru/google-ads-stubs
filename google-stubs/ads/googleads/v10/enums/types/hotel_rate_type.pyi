import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class HotelRateTypeEnum(proto.Message):
    class HotelRateType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        UNAVAILABLE: int
        PUBLIC_RATE: int
        QUALIFIED_RATE: int
        PRIVATE_RATE: int

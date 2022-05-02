import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class HotelPriceBucketEnum(proto.Message):
    class HotelPriceBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LOWEST_UNIQUE: int
        LOWEST_TIED: int
        NOT_LOWEST: int
        ONLY_PARTNER_SHOWN: int

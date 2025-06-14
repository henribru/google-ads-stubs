import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PaymentModeEnum(proto.Message):
    class PaymentMode(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLICKS: int
        CONVERSION_VALUE: int
        CONVERSIONS: int
        GUEST_STAY: int

from typing import Any

import proto

__protobuf__: Any

class PaymentModeEnum(proto.Message):
    class PaymentMode(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLICKS: int
        CONVERSION_VALUE: int
        CONVERSIONS: int
        GUEST_STAY: int

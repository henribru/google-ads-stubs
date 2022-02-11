from typing import Any

import proto

__protobuf__: Any

class MerchantCenterErrorEnum(proto.Message):
    class MerchantCenterError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MERCHANT_ID_CANNOT_BE_ACCESSED: int
        CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX: int

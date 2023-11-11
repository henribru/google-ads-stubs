from typing import Any

import proto

class MerchantCenterErrorEnum(proto.Message):
    class MerchantCenterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MERCHANT_ID_CANNOT_BE_ACCESSED = 2
        CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

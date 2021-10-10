from typing import Any

import proto

__protobuf__: Any

class PaymentsAccountErrorEnum(proto.Message):
    class PaymentsAccountError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_SUPPORTED_FOR_MANAGER_CUSTOMER: int

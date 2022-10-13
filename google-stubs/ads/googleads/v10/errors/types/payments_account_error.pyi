from typing import Any

import proto

class PaymentsAccountErrorEnum(proto.Message):
    class PaymentsAccountError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_SUPPORTED_FOR_MANAGER_CUSTOMER = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

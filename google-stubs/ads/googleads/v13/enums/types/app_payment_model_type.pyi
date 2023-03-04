from typing import Any

import proto

class AppPaymentModelTypeEnum(proto.Message):
    class AppPaymentModelType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAID = 30
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

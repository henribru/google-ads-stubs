from typing import Any

import proto

class InvoiceTypeEnum(proto.Message):
    class InvoiceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CREDIT_MEMO = 2
        INVOICE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

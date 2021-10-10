from typing import Any

import proto

__protobuf__: Any

class InvoiceTypeEnum(proto.Message):
    class InvoiceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREDIT_MEMO: int
        INVOICE: int

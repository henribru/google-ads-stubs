from typing import Any

import proto

__protobuf__: Any

class InvoiceErrorEnum(proto.Message):
    class InvoiceError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        YEAR_MONTH_TOO_OLD: int
        NOT_INVOICED_CUSTOMER: int
        BILLING_SETUP_NOT_APPROVED: int

from typing import Any

import proto

class InvoiceErrorEnum(proto.Message):
    class InvoiceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YEAR_MONTH_TOO_OLD = 2
        NOT_INVOICED_CUSTOMER = 3
        BILLING_SETUP_NOT_APPROVED = 4
        BILLING_SETUP_NOT_ON_MONTHLY_INVOICING = 5
        NON_SERVING_CUSTOMER = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

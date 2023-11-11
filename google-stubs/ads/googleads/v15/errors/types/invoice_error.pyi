from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

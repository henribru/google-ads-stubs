from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class HotelReconciliationStatusEnum(proto.Message):
    class HotelReconciliationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESERVATION_ENABLED = 2
        RECONCILIATION_NEEDED = 3
        RECONCILED = 4
        CANCELED = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class HotelReconciliationStatusEnum(proto.Message):
    class HotelReconciliationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESERVATION_ENABLED = 2
        RECONCILIATION_NEEDED = 3
        RECONCILED = 4
        CANCELED = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

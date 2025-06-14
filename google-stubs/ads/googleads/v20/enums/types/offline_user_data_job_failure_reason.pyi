import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class OfflineUserDataJobFailureReasonEnum(proto.Message):
    class OfflineUserDataJobFailureReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INSUFFICIENT_MATCHED_TRANSACTIONS = 2
        INSUFFICIENT_TRANSACTIONS = 3
        HIGH_AVERAGE_TRANSACTION_VALUE = 4
        LOW_AVERAGE_TRANSACTION_VALUE = 5
        NEWLY_OBSERVED_CURRENCY_CODE = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

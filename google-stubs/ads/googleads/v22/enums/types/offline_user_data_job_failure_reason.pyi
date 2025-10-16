from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

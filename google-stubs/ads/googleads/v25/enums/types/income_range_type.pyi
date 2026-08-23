from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class IncomeRangeTypeEnum(proto.Message):
    class IncomeRangeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INCOME_RANGE_0_50 = 510001
        INCOME_RANGE_50_60 = 510002
        INCOME_RANGE_60_70 = 510003
        INCOME_RANGE_70_80 = 510004
        INCOME_RANGE_80_90 = 510005
        INCOME_RANGE_90_UP = 510006
        INCOME_RANGE_UNDETERMINED = 510000

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

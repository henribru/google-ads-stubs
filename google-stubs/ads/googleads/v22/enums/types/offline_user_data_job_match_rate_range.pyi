from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class OfflineUserDataJobMatchRateRangeEnum(proto.Message):
    class OfflineUserDataJobMatchRateRange(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MATCH_RANGE_LESS_THAN_20 = 2
        MATCH_RANGE_20_TO_30 = 3
        MATCH_RANGE_31_TO_40 = 4
        MATCH_RANGE_41_TO_50 = 5
        MATCH_RANGE_51_TO_60 = 6
        MATCH_RANGE_61_TO_70 = 7
        MATCH_RANGE_71_TO_80 = 8
        MATCH_RANGE_81_TO_90 = 9
        MATCH_RANGE_91_TO_100 = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

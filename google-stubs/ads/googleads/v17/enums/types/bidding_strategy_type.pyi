from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BiddingStrategyTypeEnum(proto.Message):
    class BiddingStrategyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        COMMISSION = 16
        ENHANCED_CPC = 2
        FIXED_CPM = 19
        INVALID = 17
        MANUAL_CPA = 18
        MANUAL_CPC = 3
        MANUAL_CPM = 4
        MANUAL_CPV = 13
        MAXIMIZE_CONVERSIONS = 10
        MAXIMIZE_CONVERSION_VALUE = 11
        PAGE_ONE_PROMOTED = 5
        PERCENT_CPC = 12
        TARGET_CPA = 6
        TARGET_CPM = 14
        TARGET_CPV = 20
        TARGET_IMPRESSION_SHARE = 15
        TARGET_OUTRANK_SHARE = 7
        TARGET_ROAS = 8
        TARGET_SPEND = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

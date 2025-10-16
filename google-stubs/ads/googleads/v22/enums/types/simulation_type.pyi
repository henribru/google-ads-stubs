from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SimulationTypeEnum(proto.Message):
    class SimulationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CPC_BID = 2
        CPV_BID = 3
        TARGET_CPA = 4
        BID_MODIFIER = 5
        TARGET_ROAS = 6
        PERCENT_CPC_BID = 7
        TARGET_IMPRESSION_SHARE = 8
        BUDGET = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

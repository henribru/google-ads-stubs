from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class TargetCpaOptInRecommendationGoalEnum(proto.Message):
    class TargetCpaOptInRecommendationGoal(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SAME_COST = 2
        SAME_CONVERSIONS = 3
        SAME_CPA = 4
        CLOSEST_CPA = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

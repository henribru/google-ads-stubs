from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ExperimentMetricEnum(proto.Message):
    class ExperimentMetric(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICKS = 2
        IMPRESSIONS = 3
        COST = 4
        CONVERSIONS_PER_INTERACTION_RATE = 5
        COST_PER_CONVERSION = 6
        CONVERSIONS_VALUE_PER_COST = 7
        AVERAGE_CPC = 8
        CTR = 9
        INCREMENTAL_CONVERSIONS = 10
        COMPLETED_VIDEO_VIEWS = 11
        CUSTOM_ALGORITHMS = 12
        CONVERSIONS = 13
        CONVERSION_VALUE = 14

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

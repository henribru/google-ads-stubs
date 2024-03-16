from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.experiment_metric import ExperimentMetricEnum
from google.ads.googleads.v14.enums.types.experiment_metric_direction import (
    ExperimentMetricDirectionEnum,
)

_M = TypeVar("_M")

class MetricGoal(proto.Message):
    metric: ExperimentMetricEnum.ExperimentMetric
    direction: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        metric: ExperimentMetricEnum.ExperimentMetric = ...,
        direction: ExperimentMetricDirectionEnum.ExperimentMetricDirection = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["metric", "direction"]
    ) -> bool: ...

from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        metric: ExperimentMetricEnum.ExperimentMetric = ...,
        direction: ExperimentMetricDirectionEnum.ExperimentMetricDirection = ...
    ) -> None: ...

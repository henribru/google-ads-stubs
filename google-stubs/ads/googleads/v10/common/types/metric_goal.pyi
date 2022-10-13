from typing import Any

import proto

from google.ads.googleads.v10.enums.types.experiment_metric import ExperimentMetricEnum
from google.ads.googleads.v10.enums.types.experiment_metric_direction import (
    ExperimentMetricDirectionEnum,
)

class MetricGoal(proto.Message):
    metric: ExperimentMetricEnum.ExperimentMetric
    direction: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        metric: ExperimentMetricEnum.ExperimentMetric = ...,
        direction: ExperimentMetricDirectionEnum.ExperimentMetricDirection = ...
    ) -> None: ...

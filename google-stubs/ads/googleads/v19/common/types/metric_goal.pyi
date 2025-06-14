import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import experiment_metric, experiment_metric_direction

__protobuf__: Incomplete

class MetricGoal(proto.Message):
    metric: experiment_metric.ExperimentMetricEnum.ExperimentMetric
    direction: experiment_metric_direction.ExperimentMetricDirectionEnum.ExperimentMetricDirection

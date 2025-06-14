import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import metric_goal
from google.ads.googleads.v19.enums.types import async_action_status, experiment_status, experiment_type
from typing import MutableSequence

__protobuf__: Incomplete

class Experiment(proto.Message):
    resource_name: str
    experiment_id: int
    name: str
    description: str
    suffix: str
    type_: experiment_type.ExperimentTypeEnum.ExperimentType
    status: experiment_status.ExperimentStatusEnum.ExperimentStatus
    start_date: str
    end_date: str
    goals: MutableSequence[metric_goal.MetricGoal]
    long_running_operation: str
    promote_status: async_action_status.AsyncActionStatusEnum.AsyncActionStatus
    sync_enabled: bool

from typing import Any

import proto

from google.ads.googleads.v10.common.types.metric_goal import MetricGoal
from google.ads.googleads.v10.enums.types.async_action_status import (
    AsyncActionStatusEnum,
)
from google.ads.googleads.v10.enums.types.experiment_status import ExperimentStatusEnum
from google.ads.googleads.v10.enums.types.experiment_type import ExperimentTypeEnum

class Experiment(proto.Message):
    resource_name: str
    experiment_id: int
    name: str
    description: str
    suffix: str
    type_: ExperimentTypeEnum.ExperimentType
    status: ExperimentStatusEnum.ExperimentStatus
    start_date: str
    end_date: str
    goals: list[MetricGoal]
    long_running_operation: str
    promote_status: AsyncActionStatusEnum.AsyncActionStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        experiment_id: int = ...,
        name: str = ...,
        description: str = ...,
        suffix: str = ...,
        type_: ExperimentTypeEnum.ExperimentType = ...,
        status: ExperimentStatusEnum.ExperimentStatus = ...,
        start_date: str = ...,
        end_date: str = ...,
        goals: list[MetricGoal] = ...,
        long_running_operation: str = ...,
        promote_status: AsyncActionStatusEnum.AsyncActionStatus = ...
    ) -> None: ...

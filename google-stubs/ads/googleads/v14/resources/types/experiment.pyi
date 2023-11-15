from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.metric_goal import MetricGoal
from google.ads.googleads.v14.enums.types.async_action_status import (
    AsyncActionStatusEnum,
)
from google.ads.googleads.v14.enums.types.experiment_status import ExperimentStatusEnum
from google.ads.googleads.v14.enums.types.experiment_type import ExperimentTypeEnum

_M = TypeVar("_M")

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
    goals: MutableSequence[MetricGoal]
    long_running_operation: str
    promote_status: AsyncActionStatusEnum.AsyncActionStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        experiment_id: int = ...,
        name: str = ...,
        description: str = ...,
        suffix: str = ...,
        type_: ExperimentTypeEnum.ExperimentType = ...,
        status: ExperimentStatusEnum.ExperimentStatus = ...,
        start_date: str = ...,
        end_date: str = ...,
        goals: MutableSequence[MetricGoal] = ...,
        long_running_operation: str = ...,
        promote_status: AsyncActionStatusEnum.AsyncActionStatus = ...
    ) -> None: ...

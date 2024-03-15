from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.metric_goal import MetricGoal
from google.ads.googleads.v16.enums.types.async_action_status import (
    AsyncActionStatusEnum,
)
from google.ads.googleads.v16.enums.types.experiment_status import ExperimentStatusEnum
from google.ads.googleads.v16.enums.types.experiment_type import ExperimentTypeEnum

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
    sync_enabled: bool
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
        promote_status: AsyncActionStatusEnum.AsyncActionStatus = ...,
        sync_enabled: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "experiment_id", "name", "description", "suffix", "type_", "status", "start_date", "end_date", "goals", "long_running_operation", "promote_status", "sync_enabled"]) -> bool: ...  # type: ignore[override]

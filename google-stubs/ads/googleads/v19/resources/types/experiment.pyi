from google.ads.googleads.v19.enums.types.async_action_status import AsyncActionStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.metric_goal import MetricGoal
from google.ads.googleads.v19.enums.types.experiment_status import ExperimentStatusEnum
from google.ads.googleads.v19.enums.types.experiment_type import ExperimentTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., experiment_id: int = ..., name: str = ..., description: str = ..., suffix: str = ..., type_: ExperimentTypeEnum.ExperimentType = ..., status: ExperimentStatusEnum.ExperimentStatus = ..., start_date: str = ..., end_date: str = ..., goals: MutableSequence[MetricGoal] = ..., long_running_operation: str = ..., promote_status: AsyncActionStatusEnum.AsyncActionStatus = ..., sync_enabled: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "experiment_id", "name", "description", "suffix", "type_", "status", "start_date", "end_date", "goals", "long_running_operation", "promote_status", "sync_enabled"]) -> bool: ...

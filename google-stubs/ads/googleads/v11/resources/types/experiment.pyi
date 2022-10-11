import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import metric_goal as metric_goal
from google.ads.googleads.v11.enums.types import (
    async_action_status as async_action_status,
    experiment_status as experiment_status,
    experiment_type as experiment_type,
)

__protobuf__: Incomplete

class Experiment(proto.Message):
    resource_name: Incomplete
    experiment_id: Incomplete
    name: Incomplete
    description: Incomplete
    suffix: Incomplete
    type_: Incomplete
    status: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    goals: Incomplete
    long_running_operation: Incomplete
    promote_status: Incomplete

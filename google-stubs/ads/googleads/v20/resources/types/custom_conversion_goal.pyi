import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import custom_conversion_goal_status
from typing import MutableSequence

__protobuf__: Incomplete

class CustomConversionGoal(proto.Message):
    resource_name: str
    id: int
    name: str
    conversion_actions: MutableSequence[str]
    status: custom_conversion_goal_status.CustomConversionGoalStatusEnum.CustomConversionGoalStatus

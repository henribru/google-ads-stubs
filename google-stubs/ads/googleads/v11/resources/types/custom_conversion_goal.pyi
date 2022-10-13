from typing import Any

import proto

from google.ads.googleads.v11.enums.types.custom_conversion_goal_status import (
    CustomConversionGoalStatusEnum,
)

class CustomConversionGoal(proto.Message):
    resource_name: str
    id: int
    name: str
    conversion_actions: list[str]
    status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        conversion_actions: list[str] = ...,
        status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus = ...
    ) -> None: ...

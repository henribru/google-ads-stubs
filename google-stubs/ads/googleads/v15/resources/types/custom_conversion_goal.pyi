from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.custom_conversion_goal_status import (
    CustomConversionGoalStatusEnum,
)

_M = TypeVar("_M")

class CustomConversionGoal(proto.Message):
    resource_name: str
    id: int
    name: str
    conversion_actions: MutableSequence[str]
    status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        conversion_actions: MutableSequence[str] = ...,
        status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["resource_name", "id", "name", "conversion_actions", "status"],
    ) -> bool: ...

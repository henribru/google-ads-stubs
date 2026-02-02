from google.ads.googleads.v23.enums.types.custom_conversion_goal_status import CustomConversionGoalStatusEnum
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomConversionGoal(proto.Message):
    resource_name: str
    id: int
    name: str
    conversion_actions: MutableSequence[str]
    status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., name: str = ..., conversion_actions: MutableSequence[str] = ..., status: CustomConversionGoalStatusEnum.CustomConversionGoalStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "name", "conversion_actions", "status"]) -> bool: ...

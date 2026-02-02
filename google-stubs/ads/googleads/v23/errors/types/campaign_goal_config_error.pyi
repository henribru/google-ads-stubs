import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignGoalConfigErrorEnum(proto.Message):
    class CampaignGoalConfigError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOAL_NOT_FOUND = 3
        CAMPAIGN_NOT_FOUND = 4
        HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT = 9
        HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE = 10
        CUSTOMER_LIFECYCLE_OPTIMIZATION_CAMPAIGN_TYPE_NOT_SUPPORTED = 11
        CUSTOMER_NOT_ALLOWLISTED_FOR_RETENTION_ONLY = 12
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

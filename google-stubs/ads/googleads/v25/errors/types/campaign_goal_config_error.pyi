from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        CAMPAIGN_OVERRIDE_VALUES_SET_FOR_NEW_CUSTOMER_ACQUISITION_TARGET_SPECIFIC_OPTION = 13
        CAMPAIGN_OVERRIDE_HIGH_LIFETIME_VALUE_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = 14
        CANNOT_USE_INCOMPATIBLE_CLO_GOALS = 15
        LOYALTY_RETENTION_GOAL_INVALID_MODE = 16

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

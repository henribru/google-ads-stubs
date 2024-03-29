from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ExperimentArmErrorEnum(proto.Message):
    class ExperimentArmError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED = 2
        INVALID_CAMPAIGN_STATUS = 3
        DUPLICATE_EXPERIMENT_ARM_NAME = 4
        CANNOT_SET_TREATMENT_ARM_CAMPAIGN = 5
        CANNOT_MODIFY_CAMPAIGN_IDS = 6
        CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET = 7
        CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START = 8
        CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET = 9
        CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET = 10
        CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED = 11
        UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE = 12
        CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE = 13
        BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS = 14
        TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE = 15

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

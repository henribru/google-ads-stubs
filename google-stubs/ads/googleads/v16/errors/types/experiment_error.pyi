from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ExperimentErrorEnum(proto.Message):
    class ExperimentError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_SET_START_DATE_IN_PAST = 2
        END_DATE_BEFORE_START_DATE = 3
        START_DATE_TOO_FAR_IN_FUTURE = 4
        DUPLICATE_EXPERIMENT_NAME = 5
        CANNOT_MODIFY_REMOVED_EXPERIMENT = 6
        START_DATE_ALREADY_PASSED = 7
        CANNOT_SET_END_DATE_IN_PAST = 8
        CANNOT_SET_STATUS_TO_REMOVED = 9
        CANNOT_MODIFY_PAST_END_DATE = 10
        INVALID_STATUS = 11
        INVALID_CAMPAIGN_CHANNEL_TYPE = 12
        OVERLAPPING_MEMBERS_AND_DATE_RANGE = 13
        INVALID_TRIAL_ARM_TRAFFIC_SPLIT = 14
        TRAFFIC_SPLIT_OVERLAPPING = 15
        SUM_TRIAL_ARM_TRAFFIC_UNEQUALS_TO_TRIAL_TRAFFIC_SPLIT_DENOMINATOR = 16
        CANNOT_MODIFY_TRAFFIC_SPLIT_AFTER_START = 17
        EXPERIMENT_NOT_FOUND = 18
        EXPERIMENT_NOT_YET_STARTED = 19
        CANNOT_HAVE_MULTIPLE_CONTROL_ARMS = 20
        IN_DESIGN_CAMPAIGNS_NOT_SET = 21
        CANNOT_SET_STATUS_TO_GRADUATED = 22
        CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_SHARED_BUDGET = 23
        CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_CUSTOM_BUDGET = 24
        STATUS_TRANSITION_INVALID = 25
        DUPLICATE_EXPERIMENT_CAMPAIGN_NAME = 26
        CANNOT_REMOVE_IN_CREATION_EXPERIMENT = 27
        CANNOT_ADD_CAMPAIGN_WITH_DEPRECATED_AD_TYPES = 28
        CANNOT_ENABLE_SYNC_FOR_UNSUPPORTED_EXPERIMENT_TYPE = 29
        INVALID_DURATION_FOR_AN_EXPERIMENT = 30

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

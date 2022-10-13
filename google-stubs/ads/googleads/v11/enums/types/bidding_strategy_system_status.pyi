from typing import Any

import proto

class BiddingStrategySystemStatusEnum(proto.Message):
    class BiddingStrategySystemStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        LEARNING_NEW = 3
        LEARNING_SETTING_CHANGE = 4
        LEARNING_BUDGET_CHANGE = 5
        LEARNING_COMPOSITION_CHANGE = 6
        LEARNING_CONVERSION_TYPE_CHANGE = 7
        LEARNING_CONVERSION_SETTING_CHANGE = 8
        LIMITED_BY_CPC_BID_CEILING = 9
        LIMITED_BY_CPC_BID_FLOOR = 10
        LIMITED_BY_DATA = 11
        LIMITED_BY_BUDGET = 12
        LIMITED_BY_LOW_PRIORITY_SPEND = 13
        LIMITED_BY_LOW_QUALITY = 14
        LIMITED_BY_INVENTORY = 15
        MISCONFIGURED_ZERO_ELIGIBILITY = 16
        MISCONFIGURED_CONVERSION_TYPES = 17
        MISCONFIGURED_CONVERSION_SETTINGS = 18
        MISCONFIGURED_SHARED_BUDGET = 19
        MISCONFIGURED_STRATEGY_TYPE = 20
        PAUSED = 21
        UNAVAILABLE = 22
        MULTIPLE_LEARNING = 23
        MULTIPLE_LIMITED = 24
        MULTIPLE_MISCONFIGURED = 25
        MULTIPLE = 26
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

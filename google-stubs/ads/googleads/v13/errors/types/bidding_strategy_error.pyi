from typing import Any

import proto

class BiddingStrategyErrorEnum(proto.Message):
    class BiddingStrategyError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE = 3
        CANNOT_REMOVE_ASSOCIATED_STRATEGY = 4
        BIDDING_STRATEGY_NOT_SUPPORTED = 5
        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

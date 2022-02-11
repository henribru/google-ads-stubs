from typing import Any

import proto

__protobuf__: Any

class BiddingStrategyErrorEnum(proto.Message):
    class BiddingStrategyError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: int
        CANNOT_REMOVE_ASSOCIATED_STRATEGY: int
        BIDDING_STRATEGY_NOT_SUPPORTED: int
        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: int

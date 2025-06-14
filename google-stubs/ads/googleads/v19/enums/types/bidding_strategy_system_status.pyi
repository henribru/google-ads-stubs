import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BiddingStrategySystemStatusEnum(proto.Message):
    class BiddingStrategySystemStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        LEARNING_NEW: int
        LEARNING_SETTING_CHANGE: int
        LEARNING_BUDGET_CHANGE: int
        LEARNING_COMPOSITION_CHANGE: int
        LEARNING_CONVERSION_TYPE_CHANGE: int
        LEARNING_CONVERSION_SETTING_CHANGE: int
        LIMITED_BY_CPC_BID_CEILING: int
        LIMITED_BY_CPC_BID_FLOOR: int
        LIMITED_BY_DATA: int
        LIMITED_BY_BUDGET: int
        LIMITED_BY_LOW_PRIORITY_SPEND: int
        LIMITED_BY_LOW_QUALITY: int
        LIMITED_BY_INVENTORY: int
        MISCONFIGURED_ZERO_ELIGIBILITY: int
        MISCONFIGURED_CONVERSION_TYPES: int
        MISCONFIGURED_CONVERSION_SETTINGS: int
        MISCONFIGURED_SHARED_BUDGET: int
        MISCONFIGURED_STRATEGY_TYPE: int
        PAUSED: int
        UNAVAILABLE: int
        MULTIPLE_LEARNING: int
        MULTIPLE_LIMITED: int
        MULTIPLE_MISCONFIGURED: int
        MULTIPLE: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomConversionGoalErrorEnum(proto.Message):
    class CustomConversionGoalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_CONVERSION_ACTION: int
        CONVERSION_ACTION_NOT_ENABLED: int
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL: int
        CUSTOM_GOAL_DUPLICATE_NAME: int
        DUPLICATE_CONVERSION_ACTION_LIST: int
        NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL: int

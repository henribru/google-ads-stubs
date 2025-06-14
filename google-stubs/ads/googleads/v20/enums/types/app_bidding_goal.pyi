import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AppBiddingGoalEnum(proto.Message):
    class AppBiddingGoal(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME: int
        OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME: int
        OPTIMIZE_FOR_TOTAL_CONVERSION_VALUE: int
        OPTIMIZE_FOR_TARGET_IN_APP_CONVERSION: int
        OPTIMIZE_FOR_RETURN_ON_ADVERTISING_SPEND: int
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME_WITHOUT_TARGET_CPI: int
        OPTIMIZE_FOR_PRE_REGISTRATION_CONVERSION_VOLUME: int

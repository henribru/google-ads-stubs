from typing import Any

import proto

__protobuf__: Any

class AppCampaignBiddingStrategyGoalTypeEnum(proto.Message):
    class AppCampaignBiddingStrategyGoalType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPTIMIZE_INSTALLS_TARGET_INSTALL_COST: int
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST: int
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST: int
        OPTIMIZE_RETURN_ON_ADVERTISING_SPEND: int

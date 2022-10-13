from typing import Any

import proto

class AppCampaignBiddingStrategyGoalTypeEnum(proto.Message):
    class AppCampaignBiddingStrategyGoalType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTIMIZE_INSTALLS_TARGET_INSTALL_COST = 2
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST = 3
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST = 4
        OPTIMIZE_RETURN_ON_ADVERTISING_SPEND = 5
        OPTIMIZE_PRE_REGISTRATION_CONVERSION_VOLUME = 6
        OPTIMIZE_INSTALLS_WITHOUT_TARGET_INSTALL_COST = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

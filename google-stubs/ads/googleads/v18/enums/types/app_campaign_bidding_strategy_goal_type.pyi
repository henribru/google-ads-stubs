from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

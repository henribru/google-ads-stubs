from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AppBiddingGoalEnum(proto.Message):
    class AppBiddingGoal(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME = 2
        OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME = 3
        OPTIMIZE_FOR_TOTAL_CONVERSION_VALUE = 4
        OPTIMIZE_FOR_TARGET_IN_APP_CONVERSION = 5
        OPTIMIZE_FOR_RETURN_ON_ADVERTISING_SPEND = 6
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME_WITHOUT_TARGET_CPI = 7
        OPTIMIZE_FOR_PRE_REGISTRATION_CONVERSION_VOLUME = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

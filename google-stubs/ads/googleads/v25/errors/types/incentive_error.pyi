from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class IncentiveErrorEnum(proto.Message):
    class IncentiveError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_INCENTIVE_ID = 2
        MAX_INCENTIVES_REDEEMED = 3
        ACCOUNT_TOO_OLD = 4
        BILLING_COUNTRY_NOT_ELIGIBLE = 5
        USER_IS_MCC_MANAGER = 6
        USER_SUSPENDED = 7
        MAX_PENDING_INCENTIVES = 8
        ACCOUNT_HAD_RECENT_SPEND = 9
        MAX_INCENTIVES_REDEEMED_FROM_OFFER = 10
        MISMATCHING_BILLING_COUNTRY_CODE = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

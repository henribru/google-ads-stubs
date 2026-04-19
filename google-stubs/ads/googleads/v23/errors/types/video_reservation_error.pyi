from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class VideoReservationErrorEnum(proto.Message):
    class VideoReservationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW_QUOTE_REQUIRED = 2
        CAMPAIGN_END_TIME_TOO_DISTANT = 3
        BUDGET_TOO_SMALL = 4
        CAMPAIGN_DURATION_TOO_SHORT = 5
        CAMPAIGN_NOT_ENABLED = 6
        NOT_ENOUGH_AVAILABLE_INVENTORY = 7
        TARGETING_TOO_NARROW = 8
        UNSUPPORTED_AD_GROUP_TYPE = 9
        UNSUPPORTED_BID_MODIFIER = 10
        CANNOT_CHANGE_PRICING_MODEL = 11
        INCOMPATIBLE_TARGETING = 12
        UNSUPPORTED_FEATURE = 13
        MISSING_ELECTION_CERTIFICATE = 14
        CAMPAIGN_ENDED = 15
        UNSUPPORTED_BUDGET_PERIOD = 16
        EXACTLY_ONE_ENABLED_ADGROUP_REQUIRED = 17
        FREQUENCY_CAP_TOO_NARROW = 18
        TARGETED_PACK_NEEDS_DEAL = 19
        DEAL_CURRENCY_MISMATCH = 20
        CANNOT_HOLD_CONTRACT = 21
        CUSTOMER_NOT_ENABLED = 22
        CUSTOMER_NOT_ALLOWED = 23
        INVALID_ACCOUNT_TYPE = 24
        ACCOUNT_IS_MANAGER = 25
        SEASONAL_LINEUP_BOOKING_WINDOW_NOT_OPEN = 26
        SEASONAL_LINEUP_END_DATE_OFF_SEASON = 27
        SEASONAL_LINEUP_GEO_TARGETING_TOO_NARROW = 28
        NO_MARKET_RATE_CARD_OR_BASE_RATE = 29
        STALE_QUOTE = 30
        LINEUP_NOT_ALLOWED = 31
        UNSUPPORTED_BIDDING_STRATEGY = 32
        UNSUPPORTED_POSITIVE_GEO_TARGET_TYPE = 33
        VALIDATE_ONLY_REQUIRED = 34
        TOO_MANY_CAMPAIGNS = 35

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

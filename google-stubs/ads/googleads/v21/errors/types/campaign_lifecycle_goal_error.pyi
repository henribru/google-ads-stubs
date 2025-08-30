from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignLifecycleGoalErrorEnum(proto.Message):
    class CampaignLifecycleGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_MISSING = 2
        INVALID_CAMPAIGN = 3
        CUSTOMER_ACQUISITION_INVALID_OPTIMIZATION_MODE = 4
        INCOMPATIBLE_BIDDING_STRATEGY = 5
        MISSING_PURCHASE_GOAL = 6
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE = 7
        CUSTOMER_ACQUISITION_UNSUPPORTED_CAMPAIGN_TYPE = 8
        CUSTOMER_ACQUISITION_INVALID_VALUE = 9
        CUSTOMER_ACQUISITION_VALUE_MISSING = 10
        CUSTOMER_ACQUISITION_MISSING_EXISTING_CUSTOMER_DEFINITION = 11
        CUSTOMER_ACQUISITION_MISSING_HIGH_VALUE_CUSTOMER_DEFINITION = 12

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

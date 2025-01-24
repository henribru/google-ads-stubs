from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignBudgetErrorEnum(proto.Message):
    class CampaignBudgetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_BUDGET_CANNOT_BE_SHARED = 17
        CAMPAIGN_BUDGET_REMOVED = 2
        CAMPAIGN_BUDGET_IN_USE = 3
        CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE = 4
        CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET = 6
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED = 7
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME = 8
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED = 9
        CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS = 10
        DUPLICATE_NAME = 11
        MONEY_AMOUNT_IN_WRONG_CURRENCY = 12
        MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC = 13
        MONEY_AMOUNT_TOO_LARGE = 14
        NEGATIVE_MONEY_AMOUNT = 15
        NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT = 16
        TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY = 18
        INVALID_PERIOD = 19
        CANNOT_USE_ACCELERATED_DELIVERY_MODE = 20
        BUDGET_AMOUNT_MUST_BE_UNSET_FOR_CUSTOM_BUDGET_PERIOD = 21

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

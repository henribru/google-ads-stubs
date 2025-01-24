from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BillingSetupErrorEnum(proto.Message):
    class BillingSetupError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_USE_EXISTING_AND_NEW_ACCOUNT = 2
        CANNOT_REMOVE_STARTED_BILLING_SETUP = 3
        CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT = 4
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS = 5
        INVALID_PAYMENTS_ACCOUNT = 6
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY = 7
        INVALID_START_TIME_TYPE = 8
        THIRD_PARTY_ALREADY_HAS_BILLING = 9
        BILLING_SETUP_IN_PROGRESS = 10
        NO_SIGNUP_PERMISSION = 11
        CHANGE_OF_BILL_TO_IN_PROGRESS = 12
        PAYMENTS_PROFILE_NOT_FOUND = 13
        PAYMENTS_ACCOUNT_NOT_FOUND = 14
        PAYMENTS_PROFILE_INELIGIBLE = 15
        PAYMENTS_ACCOUNT_INELIGIBLE = 16
        CUSTOMER_NEEDS_INTERNAL_APPROVAL = 17
        PAYMENTS_PROFILE_NEEDS_SERVICE_AGREEMENT_ACCEPTANCE = 18
        PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH = 19
        FUTURE_START_TIME_PROHIBITED = 20
        TOO_MANY_BILLING_SETUPS_FOR_PAYMENTS_ACCOUNT = 21

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

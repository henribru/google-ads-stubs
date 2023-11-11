from typing import Any

import proto

class CustomerLifecycleGoalErrorEnum(proto.Message):
    class CustomerLifecycleGoalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_ACQUISITION_VALUE_MISSING = 2
        CUSTOMER_ACQUISITION_INVALID_VALUE = 3
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE = 4
        CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED = 5
        CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED = 6
        INVALID_EXISTING_USER_LIST = 7
        INVALID_HIGH_LIFETIME_VALUE_USER_LIST = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

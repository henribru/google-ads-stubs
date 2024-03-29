from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ConversionAdjustmentUploadErrorEnum(proto.Message):
    class ConversionAdjustmentUploadError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_RECENT_CONVERSION_ACTION = 2
        CONVERSION_ALREADY_RETRACTED = 4
        CONVERSION_NOT_FOUND = 5
        CONVERSION_EXPIRED = 6
        ADJUSTMENT_PRECEDES_CONVERSION = 7
        MORE_RECENT_RESTATEMENT_FOUND = 8
        TOO_RECENT_CONVERSION = 9
        CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE = 10
        TOO_MANY_ADJUSTMENTS_IN_REQUEST = 11
        TOO_MANY_ADJUSTMENTS = 12
        RESTATEMENT_ALREADY_EXISTS = 13
        DUPLICATE_ADJUSTMENT_IN_REQUEST = 14
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS = 15
        CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT = 16
        INVALID_USER_IDENTIFIER = 17
        UNSUPPORTED_USER_IDENTIFIER = 18
        GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET = 20
        CONVERSION_ALREADY_ENHANCED = 21
        DUPLICATE_ENHANCEMENT_IN_REQUEST = 22
        CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCEMENT = 23
        MISSING_ORDER_ID_FOR_WEBPAGE = 24
        ORDER_ID_CONTAINS_PII = 25
        INVALID_JOB_ID = 26
        NO_CONVERSION_ACTION_FOUND = 27
        INVALID_CONVERSION_ACTION_TYPE = 28

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

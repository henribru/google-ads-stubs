from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerPayPerConversionEligibilityFailureReasonEnum(proto.Message):
    class CustomerPayPerConversionEligibilityFailureReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_ENOUGH_CONVERSIONS = 2
        CONVERSION_LAG_TOO_HIGH = 3
        HAS_CAMPAIGN_WITH_SHARED_BUDGET = 4
        HAS_UPLOAD_CLICKS_CONVERSION = 5
        AVERAGE_DAILY_SPEND_TOO_HIGH = 6
        ANALYSIS_NOT_COMPLETE = 7
        OTHER = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

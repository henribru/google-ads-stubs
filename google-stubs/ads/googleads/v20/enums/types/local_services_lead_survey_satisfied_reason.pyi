from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesLeadSurveySatisfiedReasonEnum(proto.Message):
    class SurveySatisfiedReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OTHER_SATISFIED_REASON = 2
        BOOKED_CUSTOMER = 3
        LIKELY_BOOKED_CUSTOMER = 4
        SERVICE_RELATED = 5
        HIGH_VALUE_SERVICE = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

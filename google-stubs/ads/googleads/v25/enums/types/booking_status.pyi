from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BookingStatusEnum(proto.Message):
    class BookingStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BOOKED = 2
        HELD = 3
        CAMPAIGN_ENDED = 4
        HOLD_EXPIRED = 5
        BOOKING_CANCELLED = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

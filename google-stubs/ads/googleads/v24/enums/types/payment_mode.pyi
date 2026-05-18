from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PaymentModeEnum(proto.Message):
    class PaymentMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICKS = 4
        CONVERSION_VALUE = 5
        CONVERSIONS = 6
        GUEST_STAY = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

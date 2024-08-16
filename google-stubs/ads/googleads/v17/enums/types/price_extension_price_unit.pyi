from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PriceExtensionPriceUnitEnum(proto.Message):
    class PriceExtensionPriceUnit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PER_HOUR = 2
        PER_DAY = 3
        PER_WEEK = 4
        PER_MONTH = 5
        PER_YEAR = 6
        PER_NIGHT = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

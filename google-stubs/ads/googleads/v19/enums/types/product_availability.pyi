from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ProductAvailabilityEnum(proto.Message):
    class ProductAvailability(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IN_STOCK = 2
        OUT_OF_STOCK = 3
        PREORDER = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

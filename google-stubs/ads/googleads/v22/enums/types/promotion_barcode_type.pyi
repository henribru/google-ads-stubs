from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PromotionBarcodeTypeEnum(proto.Message):
    class PromotionBarcodeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AZTEC = 2
        CODABAR = 3
        CODE39 = 4
        CODE128 = 5
        DATA_MATRIX = 6
        EAN8 = 7
        EAN13 = 8
        ITF = 9
        PDF417 = 10
        UPC_A = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

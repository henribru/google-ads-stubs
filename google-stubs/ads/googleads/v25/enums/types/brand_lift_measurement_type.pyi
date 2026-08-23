from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BrandLiftMeasurementTypeEnum(proto.Message):
    class BrandLiftMeasurementType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RECALL = 2
        AWARENESS = 3
        CONSIDERATION = 4
        FAVORABILITY = 5
        PURCHASE_INTENT = 6
        CUSTOM = 7
        ASSOCIATION = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

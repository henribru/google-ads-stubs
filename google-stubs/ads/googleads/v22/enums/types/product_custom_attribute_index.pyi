from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ProductCustomAttributeIndexEnum(proto.Message):
    class ProductCustomAttributeIndex(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INDEX0 = 7
        INDEX1 = 8
        INDEX2 = 9
        INDEX3 = 10
        INDEX4 = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ProductBiddingCategoryLevelEnum(proto.Message):
    class ProductBiddingCategoryLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LEVEL1 = 2
        LEVEL2 = 3
        LEVEL3 = 4
        LEVEL4 = 5
        LEVEL5 = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(self, key: NoReturn) -> bool: ...  # type: ignore[override]

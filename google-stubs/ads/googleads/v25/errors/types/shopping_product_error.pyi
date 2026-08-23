from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ShoppingProductErrorEnum(proto.Message):
    class ShoppingProductError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MISSING_CAMPAIGN_FILTER = 2
        MISSING_AD_GROUP_FILTER = 3
        UNSUPPORTED_DATE_SEGMENTATION = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

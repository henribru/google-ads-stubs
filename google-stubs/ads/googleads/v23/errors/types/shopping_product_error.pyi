import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ShoppingProductErrorEnum(proto.Message):
    class ShoppingProductError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MISSING_CAMPAIGN_FILTER = 2
        MISSING_AD_GROUP_FILTER = 3
        UNSUPPORTED_DATE_SEGMENTATION = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

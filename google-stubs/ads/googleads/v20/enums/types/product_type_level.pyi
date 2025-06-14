import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ProductTypeLevelEnum(proto.Message):
    class ProductTypeLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LEVEL1 = 7
        LEVEL2 = 8
        LEVEL3 = 9
        LEVEL4 = 10
        LEVEL5 = 11
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

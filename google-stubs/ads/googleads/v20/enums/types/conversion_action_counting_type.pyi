import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionActionCountingTypeEnum(proto.Message):
    class ConversionActionCountingType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ONE_PER_CLICK = 2
        MANY_PER_CLICK = 3
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

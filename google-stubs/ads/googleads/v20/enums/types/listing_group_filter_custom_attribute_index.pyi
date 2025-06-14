import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ListingGroupFilterCustomAttributeIndexEnum(proto.Message):
    class ListingGroupFilterCustomAttributeIndex(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INDEX0 = 2
        INDEX1 = 3
        INDEX2 = 4
        INDEX3 = 5
        INDEX4 = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

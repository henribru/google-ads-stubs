import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class GeoTargetingRestrictionEnum(proto.Message):
    class GeoTargetingRestriction(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_OF_PRESENCE = 2
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

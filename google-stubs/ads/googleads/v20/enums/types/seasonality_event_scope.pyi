import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SeasonalityEventScopeEnum(proto.Message):
    class SeasonalityEventScope(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER = 2
        CAMPAIGN = 4
        CHANNEL = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

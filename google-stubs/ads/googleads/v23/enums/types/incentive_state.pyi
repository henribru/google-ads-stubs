import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class IncentiveStateEnum(proto.Message):
    class IncentiveState(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REDEEMED = 2
        FULFILLED = 3
        REWARD_GRANTED = 4
        EXPIRED = 5
        REWARD_EXPIRED = 6
        INVALIDATED = 7
        REWARD_EXHAUSTED = 8
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

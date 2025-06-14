import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SmartCampaignStatusEnum(proto.Message):
    class SmartCampaignStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAUSED = 2
        NOT_ELIGIBLE = 3
        PENDING = 4
        ELIGIBLE = 5
        REMOVED = 6
        ENDED = 7
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

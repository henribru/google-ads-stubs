import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UnitOfMeasureEnum(proto.Message):
    class UnitOfMeasure(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICKS = 2
        IMPRESSIONS = 3
        ACQUISITIONS = 4
        PHONE_CALLS = 5
        VIDEO_PLAYS = 6
        DAYS = 7
        AUDIO_PLAYS = 8
        ENGAGEMENTS = 9
        SECONDS = 10
        LEADS = 11
        GUEST_STAYS = 12
        HOURS = 13
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...

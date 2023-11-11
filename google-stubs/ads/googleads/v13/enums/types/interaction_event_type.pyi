from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class InteractionEventTypeEnum(proto.Message):
    class InteractionEventType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICK = 2
        ENGAGEMENT = 3
        VIDEO_VIEW = 4
        NONE = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

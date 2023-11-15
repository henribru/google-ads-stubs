from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AccessReasonEnum(proto.Message):
    class AccessReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OWNED = 2
        SHARED = 3
        LICENSED = 4
        SUBSCRIBED = 5
        AFFILIATED = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

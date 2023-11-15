from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CallTypeEnum(proto.Message):
    class CallType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MANUALLY_DIALED = 2
        HIGH_END_MOBILE_SEARCH = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

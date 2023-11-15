from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConversionCustomVariableStatusEnum(proto.Message):
    class ConversionCustomVariableStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACTIVATION_NEEDED = 2
        ENABLED = 3
        PAUSED = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

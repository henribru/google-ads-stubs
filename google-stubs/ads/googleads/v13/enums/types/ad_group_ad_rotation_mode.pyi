from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdGroupAdRotationModeEnum(proto.Message):
    class AdGroupAdRotationMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTIMIZE = 2
        ROTATE_FOREVER = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

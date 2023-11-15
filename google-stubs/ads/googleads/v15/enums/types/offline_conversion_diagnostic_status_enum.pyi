from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class OfflineConversionDiagnosticStatusEnum(proto.Message):
    class OfflineConversionDiagnosticStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXCELLENT = 2
        GOOD = 3
        NEEDS_ATTENTION = 4
        NO_RECENT_UPLOAD = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

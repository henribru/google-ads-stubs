from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CallConversionReportingStateEnum(proto.Message):
    class CallConversionReportingState(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DISABLED = 2
        USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION = 3
        USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

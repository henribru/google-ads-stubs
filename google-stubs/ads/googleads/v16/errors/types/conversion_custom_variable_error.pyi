from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ConversionCustomVariableErrorEnum(proto.Message):
    class ConversionCustomVariableError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        DUPLICATE_TAG = 3
        RESERVED_TAG = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(self, key: NoReturn) -> bool: ...  # type: ignore[override]

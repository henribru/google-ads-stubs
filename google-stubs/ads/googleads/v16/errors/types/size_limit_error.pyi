from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SizeLimitErrorEnum(proto.Message):
    class SizeLimitError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUEST_SIZE_LIMIT_EXCEEDED = 2
        RESPONSE_SIZE_LIMIT_EXCEEDED = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class NonSkippableMaxDurationEnum(proto.Message):
    class NonSkippableMaxDuration(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MAX_DURATION_FIFTEEN_SECONDS = 2
        MAX_DURATION_THIRTY_SECONDS = 3
        MAX_DURATION_SIXTY_SECONDS = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

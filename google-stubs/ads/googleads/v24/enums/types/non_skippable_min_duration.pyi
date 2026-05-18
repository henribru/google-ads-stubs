from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class NonSkippableMinDurationEnum(proto.Message):
    class NonSkippableMinDuration(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MIN_DURATION_FIVE_SECONDS = 2
        MIN_DURATION_SEVEN_SECONDS = 3
        MIN_DURATION_SIXTEEN_SECONDS = 4
        MIN_DURATION_THIRTY_ONE_SECONDS = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

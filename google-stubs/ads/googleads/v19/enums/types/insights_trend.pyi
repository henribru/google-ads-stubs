from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class InsightsTrendEnum(proto.Message):
    class InsightsTrend(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMERGING = 2
        RISING = 3
        SUSTAINED = 4
        DECLINING = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

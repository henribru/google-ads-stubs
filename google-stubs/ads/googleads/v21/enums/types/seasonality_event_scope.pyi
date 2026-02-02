from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SeasonalityEventScopeEnum(proto.Message):
    class SeasonalityEventScope(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER = 2
        CAMPAIGN = 4
        CHANNEL = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

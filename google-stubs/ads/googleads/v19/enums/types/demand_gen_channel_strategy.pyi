from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class DemandGenChannelStrategyEnum(proto.Message):
    class DemandGenChannelStrategy(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_CHANNELS = 2
        ALL_OWNED_AND_OPERATED_CHANNELS = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MatchingFunctionOperatorEnum(proto.Message):
    class MatchingFunctionOperator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IN = 2
        IDENTITY = 3
        EQUALS = 4
        AND = 5
        CONTAINS_ANY = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

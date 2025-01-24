from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordPlanNetworkEnum(proto.Message):
    class KeywordPlanNetwork(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOOGLE_SEARCH = 2
        GOOGLE_SEARCH_AND_PARTNERS = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

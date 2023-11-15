from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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

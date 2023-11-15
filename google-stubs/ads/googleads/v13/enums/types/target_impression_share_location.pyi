from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class TargetImpressionShareLocationEnum(proto.Message):
    class TargetImpressionShareLocation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ANYWHERE_ON_PAGE = 2
        TOP_OF_PAGE = 3
        ABSOLUTE_TOP_OF_PAGE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

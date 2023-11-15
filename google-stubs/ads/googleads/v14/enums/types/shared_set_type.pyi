from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SharedSetTypeEnum(proto.Message):
    class SharedSetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEGATIVE_KEYWORDS = 2
        NEGATIVE_PLACEMENTS = 3
        ACCOUNT_LEVEL_NEGATIVE_KEYWORDS = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

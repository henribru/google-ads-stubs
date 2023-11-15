from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdCustomizerPlaceholderFieldEnum(proto.Message):
    class AdCustomizerPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INTEGER = 2
        PRICE = 3
        DATE = 4
        STRING = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

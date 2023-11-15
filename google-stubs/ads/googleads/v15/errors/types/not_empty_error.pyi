from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class NotEmptyErrorEnum(proto.Message):
    class NotEmptyError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMPTY_LIST = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

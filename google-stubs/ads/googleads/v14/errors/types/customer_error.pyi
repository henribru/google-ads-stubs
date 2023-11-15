from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomerErrorEnum(proto.Message):
    class CustomerError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STATUS_CHANGE_DISALLOWED = 2
        ACCOUNT_NOT_SET_UP = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

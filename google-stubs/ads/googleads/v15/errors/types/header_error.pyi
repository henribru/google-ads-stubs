from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class HeaderErrorEnum(proto.Message):
    class HeaderError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_LOGIN_CUSTOMER_ID = 3
        INVALID_LINKED_CUSTOMER_ID = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

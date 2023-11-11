from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class UserDataErrorEnum(proto.Message):
    class UserDataError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED = 2
        TOO_MANY_USER_IDENTIFIERS = 3
        USER_LIST_NOT_APPLICABLE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

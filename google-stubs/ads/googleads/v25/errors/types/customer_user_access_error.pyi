from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerUserAccessErrorEnum(proto.Message):
    class CustomerUserAccessError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_USER_ID = 2
        REMOVAL_DISALLOWED = 3
        DISALLOWED_ACCESS_ROLE = 4
        LAST_ADMIN_USER_OF_SERVING_CUSTOMER = 5
        LAST_ADMIN_USER_OF_MANAGER = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SharedSetErrorEnum(proto.Message):
    class SharedSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE = 2
        DUPLICATE_NAME = 3
        SHARED_SET_REMOVED = 4
        SHARED_SET_IN_USE = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

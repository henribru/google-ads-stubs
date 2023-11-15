from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ResourceChangeOperationEnum(proto.Message):
    class ResourceChangeOperation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CREATE = 2
        UPDATE = 3
        REMOVE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

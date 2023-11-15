from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class NewResourceCreationErrorEnum(proto.Message):
    class NewResourceCreationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_SET_ID_FOR_CREATE = 2
        DUPLICATE_TEMP_IDS = 3
        TEMP_ID_RESOURCE_HAD_ERRORS = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

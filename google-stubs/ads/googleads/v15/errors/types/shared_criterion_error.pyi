from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class SharedCriterionErrorEnum(proto.Message):
    class SharedCriterionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

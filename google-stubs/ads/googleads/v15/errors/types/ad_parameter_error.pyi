from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdParameterErrorEnum(proto.Message):
    class AdParameterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_CRITERION_MUST_BE_KEYWORD = 2
        INVALID_INSERTION_TEXT_FORMAT = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

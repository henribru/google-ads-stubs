from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ParentalStatusTypeEnum(proto.Message):
    class ParentalStatusType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PARENT = 300
        NOT_A_PARENT = 301
        UNDETERMINED = 302
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

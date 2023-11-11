from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LeadFormDesiredIntentEnum(proto.Message):
    class LeadFormDesiredIntent(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOW_INTENT = 2
        HIGH_INTENT = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

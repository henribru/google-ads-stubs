from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AndroidPrivacyInteractionTypeEnum(proto.Message):
    class AndroidPrivacyInteractionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICK = 2
        ENGAGED_VIEW = 3
        VIEW = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

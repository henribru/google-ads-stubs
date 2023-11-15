from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FeedOriginEnum(proto.Message):
    class FeedOrigin(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        USER = 2
        GOOGLE = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

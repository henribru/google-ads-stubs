from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class BrandStateEnum(proto.Message):
    class BrandState(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        DEPRECATED = 3
        UNVERIFIED = 4
        APPROVED = 5
        CANCELLED = 6
        REJECTED = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

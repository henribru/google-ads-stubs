from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AssetGroupPrimaryStatusEnum(proto.Message):
    class AssetGroupPrimaryStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        PAUSED = 3
        REMOVED = 4
        NOT_ELIGIBLE = 5
        LIMITED = 6
        PENDING = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

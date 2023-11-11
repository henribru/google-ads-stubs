from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FeedItemTargetTypeEnum(proto.Message):
    class FeedItemTargetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN = 2
        AD_GROUP = 3
        CRITERION = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConvertingUserPriorEngagementTypeAndLtvBucketEnum(proto.Message):
    class ConvertingUserPriorEngagementTypeAndLtvBucket(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 2
        RETURNING = 3
        NEW_AND_HIGH_LTV = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

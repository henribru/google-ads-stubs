from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdSharingErrorEnum(proto.Message):
    class AdSharingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_ALREADY_CONTAINS_AD = 2
        INCOMPATIBLE_AD_UNDER_AD_GROUP = 3
        CANNOT_SHARE_INACTIVE_AD = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

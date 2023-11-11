from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConversionTrackingStatusEnum(proto.Message):
    class ConversionTrackingStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_CONVERSION_TRACKED = 2
        CONVERSION_TRACKING_MANAGED_BY_SELF = 3
        CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER = 4
        CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

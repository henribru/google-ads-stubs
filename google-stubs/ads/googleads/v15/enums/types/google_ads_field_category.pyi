from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class GoogleAdsFieldCategoryEnum(proto.Message):
    class GoogleAdsFieldCategory(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE = 2
        ATTRIBUTE = 3
        SEGMENT = 5
        METRIC = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class BrandSafetySuitabilityEnum(proto.Message):
    class BrandSafetySuitability(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXPANDED_INVENTORY = 2
        STANDARD_INVENTORY = 3
        LIMITED_INVENTORY = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

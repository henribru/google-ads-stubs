from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LinkedProductTypeEnum(proto.Message):
    class LinkedProductType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DATA_PARTNER = 2
        GOOGLE_ADS = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomizerAttributeTypeEnum(proto.Message):
    class CustomizerAttributeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT = 2
        NUMBER = 3
        PRICE = 4
        PERCENT = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

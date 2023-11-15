from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class HotelDateSelectionTypeEnum(proto.Message):
    class HotelDateSelectionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT_SELECTION = 50
        USER_SELECTED = 51
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

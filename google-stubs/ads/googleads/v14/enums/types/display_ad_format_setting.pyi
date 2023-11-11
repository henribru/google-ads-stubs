from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class DisplayAdFormatSettingEnum(proto.Message):
    class DisplayAdFormatSetting(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_FORMATS = 2
        NON_NATIVE = 3
        NATIVE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

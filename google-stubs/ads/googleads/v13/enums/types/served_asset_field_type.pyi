from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ServedAssetFieldTypeEnum(proto.Message):
    class ServedAssetFieldType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADLINE_1 = 2
        HEADLINE_2 = 3
        HEADLINE_3 = 4
        DESCRIPTION_1 = 5
        DESCRIPTION_2 = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

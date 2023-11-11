from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ImagePlaceholderFieldEnum(proto.Message):
    class ImagePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_ID = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

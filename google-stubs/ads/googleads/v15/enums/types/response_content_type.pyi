from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ResponseContentTypeEnum(proto.Message):
    class ResponseContentType(proto.Enum):
        UNSPECIFIED = 0
        RESOURCE_NAME_ONLY = 1
        MUTABLE_RESOURCE = 2
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

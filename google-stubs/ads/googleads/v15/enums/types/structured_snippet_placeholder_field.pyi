from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class StructuredSnippetPlaceholderFieldEnum(proto.Message):
    class StructuredSnippetPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADER = 2
        SNIPPETS = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

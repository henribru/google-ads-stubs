from typing import Any

import proto

class StructuredSnippetPlaceholderFieldEnum(proto.Message):
    class StructuredSnippetPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADER = 2
        SNIPPETS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

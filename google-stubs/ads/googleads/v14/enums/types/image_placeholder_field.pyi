from typing import Any

import proto

class ImagePlaceholderFieldEnum(proto.Message):
    class ImagePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ASSET_ID = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

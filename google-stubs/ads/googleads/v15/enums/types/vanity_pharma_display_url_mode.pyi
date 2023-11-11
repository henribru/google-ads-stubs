from typing import Any

import proto

class VanityPharmaDisplayUrlModeEnum(proto.Message):
    class VanityPharmaDisplayUrlMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MANUFACTURER_WEBSITE_URL = 2
        WEBSITE_DESCRIPTION = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class CallTrackingDisplayLocationEnum(proto.Message):
    class CallTrackingDisplayLocation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD = 2
        LANDING_PAGE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

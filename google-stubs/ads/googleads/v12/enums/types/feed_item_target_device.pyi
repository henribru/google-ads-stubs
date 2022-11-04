from typing import Any

import proto

class FeedItemTargetDeviceEnum(proto.Message):
    class FeedItemTargetDevice(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MOBILE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

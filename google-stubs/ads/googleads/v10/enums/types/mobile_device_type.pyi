from typing import Any

import proto

class MobileDeviceTypeEnum(proto.Message):
    class MobileDeviceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MOBILE = 2
        TABLET = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

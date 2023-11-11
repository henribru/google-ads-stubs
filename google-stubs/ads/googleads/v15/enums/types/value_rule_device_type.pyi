from typing import Any

import proto

class ValueRuleDeviceTypeEnum(proto.Message):
    class ValueRuleDeviceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MOBILE = 2
        DESKTOP = 3
        TABLET = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

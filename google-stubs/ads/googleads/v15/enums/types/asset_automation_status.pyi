from typing import Any

import proto

class AssetAutomationStatusEnum(proto.Message):
    class AssetAutomationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPTED_IN = 2
        OPTED_OUT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

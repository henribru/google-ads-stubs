from typing import Any

import proto

class AssetAutomationTypeEnum(proto.Message):
    class AssetAutomationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT_ASSET_AUTOMATION = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

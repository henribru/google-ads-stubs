from typing import Any

import proto

class PlacementTypeEnum(proto.Message):
    class PlacementType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBSITE = 2
        MOBILE_APP_CATEGORY = 3
        MOBILE_APPLICATION = 4
        YOUTUBE_VIDEO = 5
        YOUTUBE_CHANNEL = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

__protobuf__: Any

class PlacementTypeEnum(proto.Message):
    class PlacementType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WEBSITE: int
        MOBILE_APP_CATEGORY: int
        MOBILE_APPLICATION: int
        YOUTUBE_VIDEO: int
        YOUTUBE_CHANNEL: int

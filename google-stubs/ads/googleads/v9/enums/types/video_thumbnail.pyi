from typing import Any

import proto

__protobuf__: Any

class VideoThumbnailEnum(proto.Message):
    class VideoThumbnail(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DEFAULT_THUMBNAIL: int
        THUMBNAIL_1: int
        THUMBNAIL_2: int
        THUMBNAIL_3: int

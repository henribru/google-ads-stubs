from typing import Any

import proto

__protobuf__: Any

class MediaTypeEnum(proto.Message):
    class MediaType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IMAGE: int
        ICON: int
        MEDIA_BUNDLE: int
        AUDIO: int
        VIDEO: int
        DYNAMIC_IMAGE: int

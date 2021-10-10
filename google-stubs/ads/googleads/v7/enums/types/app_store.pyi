from typing import Any

import proto

__protobuf__: Any

class AppStoreEnum(proto.Message):
    class AppStore(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPLE_ITUNES: int
        GOOGLE_PLAY: int

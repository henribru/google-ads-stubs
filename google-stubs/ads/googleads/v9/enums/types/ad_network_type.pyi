from typing import Any

import proto

__protobuf__: Any

class AdNetworkTypeEnum(proto.Message):
    class AdNetworkType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH: int
        SEARCH_PARTNERS: int
        CONTENT: int
        YOUTUBE_SEARCH: int
        YOUTUBE_WATCH: int
        MIXED: int

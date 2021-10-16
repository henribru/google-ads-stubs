from typing import Any

import proto

__protobuf__: Any

class SearchTermMatchTypeEnum(proto.Message):
    class SearchTermMatchType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BROAD: int
        EXACT: int
        PHRASE: int
        NEAR_EXACT: int
        NEAR_PHRASE: int

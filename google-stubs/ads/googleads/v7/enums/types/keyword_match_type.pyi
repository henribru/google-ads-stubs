from typing import Any

import proto

__protobuf__: Any

class KeywordMatchTypeEnum(proto.Message):
    class KeywordMatchType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXACT: int
        PHRASE: int
        BROAD: int

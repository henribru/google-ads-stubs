from typing import Any

import proto

__protobuf__: Any

class SharedSetTypeEnum(proto.Message):
    class SharedSetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NEGATIVE_KEYWORDS: int
        NEGATIVE_PLACEMENTS: int

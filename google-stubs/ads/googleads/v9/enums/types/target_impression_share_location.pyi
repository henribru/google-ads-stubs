from typing import Any

import proto

__protobuf__: Any

class TargetImpressionShareLocationEnum(proto.Message):
    class TargetImpressionShareLocation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ANYWHERE_ON_PAGE: int
        TOP_OF_PAGE: int
        ABSOLUTE_TOP_OF_PAGE: int

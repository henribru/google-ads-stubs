from typing import Any

import proto

__protobuf__: Any

class CustomAudienceMemberTypeEnum(proto.Message):
    class CustomAudienceMemberType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        KEYWORD: int
        URL: int
        PLACE_CATEGORY: int
        APP: int

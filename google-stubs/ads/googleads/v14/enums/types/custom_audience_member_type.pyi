from typing import Any

import proto

class CustomAudienceMemberTypeEnum(proto.Message):
    class CustomAudienceMemberType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        KEYWORD = 2
        URL = 3
        PLACE_CATEGORY = 4
        APP = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

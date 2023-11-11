from typing import Any

import proto

class ChainRelationshipTypeEnum(proto.Message):
    class ChainRelationshipType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AUTO_DEALERS = 2
        GENERAL_RETAILERS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

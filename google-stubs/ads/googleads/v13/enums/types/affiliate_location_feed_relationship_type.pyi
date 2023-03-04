from typing import Any

import proto

class AffiliateLocationFeedRelationshipTypeEnum(proto.Message):
    class AffiliateLocationFeedRelationshipType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GENERAL_RETAILER = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

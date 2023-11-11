from typing import Any

import proto

class LocationOwnershipTypeEnum(proto.Message):
    class LocationOwnershipType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_OWNER = 2
        AFFILIATE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

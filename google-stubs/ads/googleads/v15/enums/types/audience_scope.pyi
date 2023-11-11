from typing import Any

import proto

class AudienceScopeEnum(proto.Message):
    class AudienceScope(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOMER = 2
        ASSET_GROUP = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

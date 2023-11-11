from typing import Any

import proto

class SkAdNetworkUserTypeEnum(proto.Message):
    class SkAdNetworkUserType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        NEW_INSTALLER = 3
        REINSTALLER = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class SkAdNetworkAttributionCreditEnum(proto.Message):
    class SkAdNetworkAttributionCredit(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNAVAILABLE = 2
        WON = 3
        CONTRIBUTED = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

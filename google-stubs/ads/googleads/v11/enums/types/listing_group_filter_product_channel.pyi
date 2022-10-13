from typing import Any

import proto

class ListingGroupFilterProductChannelEnum(proto.Message):
    class ListingGroupFilterProductChannel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ONLINE = 2
        LOCAL = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class ExtensionTypeEnum(proto.Message):
    class ExtensionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NONE = 2
        APP = 3
        CALL = 4
        CALLOUT = 5
        MESSAGE = 6
        PRICE = 7
        PROMOTION = 8
        SITELINK = 10
        STRUCTURED_SNIPPET = 11
        LOCATION = 12
        AFFILIATE_LOCATION = 13
        HOTEL_CALLOUT = 15
        IMAGE = 16
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

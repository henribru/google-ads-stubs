from typing import Any

import proto

class PlaceholderTypeEnum(proto.Message):
    class PlaceholderType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SITELINK = 2
        CALL = 3
        APP = 4
        LOCATION = 5
        AFFILIATE_LOCATION = 6
        CALLOUT = 7
        STRUCTURED_SNIPPET = 8
        MESSAGE = 9
        PRICE = 10
        PROMOTION = 11
        AD_CUSTOMIZER = 12
        DYNAMIC_EDUCATION = 13
        DYNAMIC_FLIGHT = 14
        DYNAMIC_CUSTOM = 15
        DYNAMIC_HOTEL = 16
        DYNAMIC_REAL_ESTATE = 17
        DYNAMIC_TRAVEL = 18
        DYNAMIC_LOCAL = 19
        DYNAMIC_JOB = 20
        IMAGE = 21
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

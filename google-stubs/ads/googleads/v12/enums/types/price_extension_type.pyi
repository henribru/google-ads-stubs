from typing import Any

import proto

class PriceExtensionTypeEnum(proto.Message):
    class PriceExtensionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BRANDS = 2
        EVENTS = 3
        LOCATIONS = 4
        NEIGHBORHOODS = 5
        PRODUCT_CATEGORIES = 6
        PRODUCT_TIERS = 7
        SERVICES = 8
        SERVICE_CATEGORIES = 9
        SERVICE_TIERS = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

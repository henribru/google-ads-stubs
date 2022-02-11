from typing import Any

import proto

__protobuf__: Any

class PriceExtensionTypeEnum(proto.Message):
    class PriceExtensionType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BRANDS: int
        EVENTS: int
        LOCATIONS: int
        NEIGHBORHOODS: int
        PRODUCT_CATEGORIES: int
        PRODUCT_TIERS: int
        SERVICES: int
        SERVICE_CATEGORIES: int
        SERVICE_TIERS: int

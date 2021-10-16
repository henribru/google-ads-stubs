from typing import Any

import proto

__protobuf__: Any

class BrandSafetySuitabilityEnum(proto.Message):
    class BrandSafetySuitability(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXPANDED_INVENTORY: int
        STANDARD_INVENTORY: int
        LIMITED_INVENTORY: int

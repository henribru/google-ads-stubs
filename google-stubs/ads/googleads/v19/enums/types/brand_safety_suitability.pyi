import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BrandSafetySuitabilityEnum(proto.Message):
    class BrandSafetySuitability(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXPANDED_INVENTORY: int
        STANDARD_INVENTORY: int
        LIMITED_INVENTORY: int

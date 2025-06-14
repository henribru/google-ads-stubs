import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ShoppingProductErrorEnum(proto.Message):
    class ShoppingProductError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MISSING_CAMPAIGN_FILTER: int
        MISSING_AD_GROUP_FILTER: int
        UNSUPPORTED_DATE_SEGMENTATION: int

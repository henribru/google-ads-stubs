import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionTrackingStatusEnum(proto.Message):
    class ConversionTrackingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NOT_CONVERSION_TRACKED: int
        CONVERSION_TRACKING_MANAGED_BY_SELF: int
        CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER: int
        CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER: int

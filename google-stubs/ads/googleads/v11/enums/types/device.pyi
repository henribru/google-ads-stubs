import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DeviceEnum(proto.Message):
    class Device(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MOBILE: int
        TABLET: int
        DESKTOP: int
        CONNECTED_TV: int
        OTHER: int

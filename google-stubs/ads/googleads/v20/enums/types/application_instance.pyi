import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ApplicationInstanceEnum(proto.Message):
    class ApplicationInstance(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DEVELOPMENT_AND_TESTING: int
        PRODUCTION: int

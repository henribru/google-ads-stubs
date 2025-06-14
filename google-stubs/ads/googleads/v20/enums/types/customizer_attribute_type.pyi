import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomizerAttributeTypeEnum(proto.Message):
    class CustomizerAttributeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TEXT: int
        NUMBER: int
        PRICE: int
        PERCENT: int

import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionCustomVariableErrorEnum(proto.Message):
    class ConversionCustomVariableError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        DUPLICATE_TAG: int
        RESERVED_TAG: int

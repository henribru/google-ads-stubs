import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdParameterErrorEnum(proto.Message):
    class AdParameterError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_CRITERION_MUST_BE_KEYWORD: int
        INVALID_INSERTION_TEXT_FORMAT: int

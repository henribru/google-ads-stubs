import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LanguageCodeErrorEnum(proto.Message):
    class LanguageCodeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LANGUAGE_CODE_NOT_FOUND: int
        INVALID_LANGUAGE_CODE: int

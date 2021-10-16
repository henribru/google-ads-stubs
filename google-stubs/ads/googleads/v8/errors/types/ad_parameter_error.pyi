from typing import Any

import proto

__protobuf__: Any

class AdParameterErrorEnum(proto.Message):
    class AdParameterError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_CRITERION_MUST_BE_KEYWORD: int
        INVALID_INSERTION_TEXT_FORMAT: int

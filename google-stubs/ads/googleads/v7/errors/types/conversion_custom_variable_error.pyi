from typing import Any

import proto

__protobuf__: Any

class ConversionCustomVariableErrorEnum(proto.Message):
    class ConversionCustomVariableError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        DUPLICATE_TAG: int

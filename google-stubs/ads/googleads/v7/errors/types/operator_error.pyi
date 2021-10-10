from typing import Any

import proto

__protobuf__: Any

class OperatorErrorEnum(proto.Message):
    class OperatorError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPERATOR_NOT_SUPPORTED: int

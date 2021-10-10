from typing import Any

import proto

__protobuf__: Any

class MatchingFunctionOperatorEnum(proto.Message):
    class MatchingFunctionOperator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IN: int
        IDENTITY: int
        EQUALS: int
        AND: int
        CONTAINS_ANY: int

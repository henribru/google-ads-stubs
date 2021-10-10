from typing import Any

import proto

__protobuf__: Any

class ValueRuleOperationEnum(proto.Message):
    class ValueRuleOperation(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
        MULTIPLY: int
        SET: int

from typing import Any

import proto

__protobuf__: Any

class TargetingSetting(proto.Message):
    target_restrictions: Any
    target_restriction_operations: Any

class TargetRestriction(proto.Message):
    targeting_dimension: Any
    bid_only: Any

class TargetRestrictionOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
        REMOVE: int
    operator: Any
    value: Any

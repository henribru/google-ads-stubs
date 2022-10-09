import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class TargetingSetting(proto.Message):
    target_restrictions: Incomplete
    target_restriction_operations: Incomplete

class TargetRestriction(proto.Message):
    targeting_dimension: Incomplete
    bid_only: Incomplete

class TargetRestrictionOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
        REMOVE: int
    operator: Incomplete
    value: Incomplete

import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import targeting_dimension as gage_targeting_dimension
from typing import MutableSequence

__protobuf__: Incomplete

class TargetingSetting(proto.Message):
    target_restrictions: MutableSequence['TargetRestriction']
    target_restriction_operations: MutableSequence['TargetRestrictionOperation']

class TargetRestriction(proto.Message):
    targeting_dimension: gage_targeting_dimension.TargetingDimensionEnum.TargetingDimension
    bid_only: bool

class TargetRestrictionOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADD: int
        REMOVE: int
    operator: Operator
    value: TargetRestriction

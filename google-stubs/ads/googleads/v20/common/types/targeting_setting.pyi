from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.targeting_dimension import TargetingDimensionEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class TargetRestriction(proto.Message):
    targeting_dimension: TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., targeting_dimension: TargetingDimensionEnum.TargetingDimension = ..., bid_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["targeting_dimension", "bid_only"]) -> bool: ...
class TargetRestrictionOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
        REMOVE = 3
    operator: TargetRestrictionOperation.Operator
    value: TargetRestriction
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., operator: TargetRestrictionOperation.Operator = ..., value: TargetRestriction = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["operator", "value"]) -> bool: ...
class TargetingSetting(proto.Message):
    target_restrictions: MutableSequence[TargetRestriction]
    target_restriction_operations: MutableSequence[TargetRestrictionOperation]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., target_restrictions: MutableSequence[TargetRestriction] = ..., target_restriction_operations: MutableSequence[TargetRestrictionOperation] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["target_restrictions", "target_restriction_operations"]) -> bool: ...

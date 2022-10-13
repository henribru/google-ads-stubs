from typing import Any

import proto

from google.ads.googleads.v10.enums.types.targeting_dimension import (
    TargetingDimensionEnum,
)

class TargetRestriction(proto.Message):
    targeting_dimension: TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        targeting_dimension: TargetingDimensionEnum.TargetingDimension = ...,
        bid_only: bool = ...
    ) -> None: ...

class TargetRestrictionOperation(proto.Message):
    class Operator(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADD = 2
        REMOVE = 3
    operator: TargetRestrictionOperation.Operator
    value: TargetRestriction
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: TargetRestrictionOperation.Operator = ...,
        value: TargetRestriction = ...
    ) -> None: ...

class TargetingSetting(proto.Message):
    target_restrictions: list[TargetRestriction]
    target_restriction_operations: list[TargetRestrictionOperation]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_restrictions: list[TargetRestriction] = ...,
        target_restriction_operations: list[TargetRestrictionOperation] = ...
    ) -> None: ...

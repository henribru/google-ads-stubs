from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.targeting_dimension import (
    TargetingDimensionEnum,
)

_M = TypeVar("_M")

class TargetRestriction(proto.Message):
    targeting_dimension: TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        operator: TargetRestrictionOperation.Operator = ...,
        value: TargetRestriction = ...
    ) -> None: ...

class TargetingSetting(proto.Message):
    target_restrictions: MutableSequence[TargetRestriction]
    target_restriction_operations: MutableSequence[TargetRestrictionOperation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_restrictions: MutableSequence[TargetRestriction] = ...,
        target_restriction_operations: MutableSequence[TargetRestrictionOperation] = ...
    ) -> None: ...

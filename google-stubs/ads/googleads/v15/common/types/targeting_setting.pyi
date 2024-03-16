from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.targeting_dimension import (
    TargetingDimensionEnum,
)

_M = TypeVar("_M")

class TargetRestriction(proto.Message):
    targeting_dimension: TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        targeting_dimension: TargetingDimensionEnum.TargetingDimension = ...,
        bid_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["targeting_dimension", "bid_only"]
    ) -> bool: ...

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
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        operator: TargetRestrictionOperation.Operator = ...,
        value: TargetRestriction = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["operator", "value"]
    ) -> bool: ...

class TargetingSetting(proto.Message):
    target_restrictions: MutableSequence[TargetRestriction]
    target_restriction_operations: MutableSequence[TargetRestrictionOperation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_restrictions: MutableSequence[TargetRestriction] = ...,
        target_restriction_operations: MutableSequence[
            TargetRestrictionOperation
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["target_restrictions", "target_restriction_operations"]
    ) -> bool: ...

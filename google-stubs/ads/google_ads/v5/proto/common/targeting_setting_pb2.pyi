# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    cast as typing___cast,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.targeting_dimension_pb2 import (
    TargetingDimensionEnum as google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TargetingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_restrictions(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___TargetRestriction
    ]: ...
    @property
    def target_restriction_operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___TargetRestrictionOperation
    ]: ...
    def __init__(
        self,
        *,
        target_restrictions: typing___Optional[
            typing___Iterable[type___TargetRestriction]
        ] = None,
        target_restriction_operations: typing___Optional[
            typing___Iterable[type___TargetRestrictionOperation]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "target_restriction_operations",
            b"target_restriction_operations",
            "target_restrictions",
            b"target_restrictions",
        ],
    ) -> None: ...

type___TargetingSetting = TargetingSetting

class TargetRestriction(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    targeting_dimension: google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimensionValue = ...
    bid_only: builtin___bool = ...
    def __init__(
        self,
        *,
        targeting_dimension: typing___Optional[
            google___ads___googleads___v5___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimensionValue
        ] = None,
        bid_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_bid_only", b"_bid_only", "bid_only", b"bid_only"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_bid_only",
            b"_bid_only",
            "bid_only",
            b"bid_only",
            "targeting_dimension",
            b"targeting_dimension",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_bid_only", b"_bid_only"]
    ) -> typing_extensions___Literal["bid_only"]: ...

type___TargetRestriction = TargetRestriction

class TargetRestrictionOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    OperatorValue = typing___NewType("OperatorValue", builtin___int)
    type___OperatorValue = OperatorValue
    Operator: _Operator
    class _Operator(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            TargetRestrictionOperation.OperatorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(TargetRestrictionOperation.OperatorValue, 0)
        UNKNOWN = typing___cast(TargetRestrictionOperation.OperatorValue, 1)
        ADD = typing___cast(TargetRestrictionOperation.OperatorValue, 2)
        REMOVE = typing___cast(TargetRestrictionOperation.OperatorValue, 3)
    UNSPECIFIED = typing___cast(TargetRestrictionOperation.OperatorValue, 0)
    UNKNOWN = typing___cast(TargetRestrictionOperation.OperatorValue, 1)
    ADD = typing___cast(TargetRestrictionOperation.OperatorValue, 2)
    REMOVE = typing___cast(TargetRestrictionOperation.OperatorValue, 3)
    type___Operator = Operator

    operator: type___TargetRestrictionOperation.OperatorValue = ...
    @property
    def value(self) -> type___TargetRestriction: ...
    def __init__(
        self,
        *,
        operator: typing___Optional[
            type___TargetRestrictionOperation.OperatorValue
        ] = None,
        value: typing___Optional[type___TargetRestriction] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["value", b"value"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operator", b"operator", "value", b"value"
        ],
    ) -> None: ...

type___TargetRestrictionOperation = TargetRestrictionOperation
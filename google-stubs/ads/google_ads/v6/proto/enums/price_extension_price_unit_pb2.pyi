# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class PriceExtensionPriceUnitEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PriceExtensionPriceUnitValue = typing___NewType(
        "PriceExtensionPriceUnitValue", builtin___int
    )
    type___PriceExtensionPriceUnitValue = PriceExtensionPriceUnitValue
    PriceExtensionPriceUnit: _PriceExtensionPriceUnit
    class _PriceExtensionPriceUnit(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 0
        )
        UNKNOWN = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 1
        )
        PER_HOUR = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 2
        )
        PER_DAY = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 3
        )
        PER_WEEK = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 4
        )
        PER_MONTH = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 5
        )
        PER_YEAR = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 6
        )
        PER_NIGHT = typing___cast(
            PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 7
        )
    UNSPECIFIED = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 0
    )
    UNKNOWN = typing___cast(PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 1)
    PER_HOUR = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 2
    )
    PER_DAY = typing___cast(PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 3)
    PER_WEEK = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 4
    )
    PER_MONTH = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 5
    )
    PER_YEAR = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 6
    )
    PER_NIGHT = typing___cast(
        PriceExtensionPriceUnitEnum.PriceExtensionPriceUnitValue, 7
    )
    type___PriceExtensionPriceUnit = PriceExtensionPriceUnit
    def __init__(self,) -> None: ...

type___PriceExtensionPriceUnitEnum = PriceExtensionPriceUnitEnum

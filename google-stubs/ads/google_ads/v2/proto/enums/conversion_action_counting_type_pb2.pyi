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

class ConversionActionCountingTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionActionCountingTypeValue = typing___NewType(
        "ConversionActionCountingTypeValue", builtin___int
    )
    type___ConversionActionCountingTypeValue = ConversionActionCountingTypeValue
    ConversionActionCountingType: _ConversionActionCountingType
    class _ConversionActionCountingType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 0
        )
        UNKNOWN = typing___cast(
            ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 1
        )
        ONE_PER_CLICK = typing___cast(
            ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 2
        )
        MANY_PER_CLICK = typing___cast(
            ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 3
        )
    UNSPECIFIED = typing___cast(
        ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 0
    )
    UNKNOWN = typing___cast(
        ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 1
    )
    ONE_PER_CLICK = typing___cast(
        ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 2
    )
    MANY_PER_CLICK = typing___cast(
        ConversionActionCountingTypeEnum.ConversionActionCountingTypeValue, 3
    )
    type___ConversionActionCountingType = ConversionActionCountingType
    def __init__(self,) -> None: ...

type___ConversionActionCountingTypeEnum = ConversionActionCountingTypeEnum

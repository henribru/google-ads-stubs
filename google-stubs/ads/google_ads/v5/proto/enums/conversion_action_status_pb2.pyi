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

class ConversionActionStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionActionStatusValue = typing___NewType(
        "ConversionActionStatusValue", builtin___int
    )
    type___ConversionActionStatusValue = ConversionActionStatusValue
    ConversionActionStatus: _ConversionActionStatus
    class _ConversionActionStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionActionStatusEnum.ConversionActionStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ConversionActionStatusEnum.ConversionActionStatusValue, 0
        )
        UNKNOWN = typing___cast(
            ConversionActionStatusEnum.ConversionActionStatusValue, 1
        )
        ENABLED = typing___cast(
            ConversionActionStatusEnum.ConversionActionStatusValue, 2
        )
        REMOVED = typing___cast(
            ConversionActionStatusEnum.ConversionActionStatusValue, 3
        )
        HIDDEN = typing___cast(
            ConversionActionStatusEnum.ConversionActionStatusValue, 4
        )
    UNSPECIFIED = typing___cast(
        ConversionActionStatusEnum.ConversionActionStatusValue, 0
    )
    UNKNOWN = typing___cast(ConversionActionStatusEnum.ConversionActionStatusValue, 1)
    ENABLED = typing___cast(ConversionActionStatusEnum.ConversionActionStatusValue, 2)
    REMOVED = typing___cast(ConversionActionStatusEnum.ConversionActionStatusValue, 3)
    HIDDEN = typing___cast(ConversionActionStatusEnum.ConversionActionStatusValue, 4)
    type___ConversionActionStatus = ConversionActionStatus
    def __init__(self,) -> None: ...

type___ConversionActionStatusEnum = ConversionActionStatusEnum

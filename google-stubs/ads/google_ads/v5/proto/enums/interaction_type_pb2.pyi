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

class InteractionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    InteractionTypeValue = typing___NewType("InteractionTypeValue", builtin___int)
    type___InteractionTypeValue = InteractionTypeValue
    InteractionType: _InteractionType
    class _InteractionType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            InteractionTypeEnum.InteractionTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(InteractionTypeEnum.InteractionTypeValue, 0)
        UNKNOWN = typing___cast(InteractionTypeEnum.InteractionTypeValue, 1)
        CALLS = typing___cast(InteractionTypeEnum.InteractionTypeValue, 8000)
    UNSPECIFIED = typing___cast(InteractionTypeEnum.InteractionTypeValue, 0)
    UNKNOWN = typing___cast(InteractionTypeEnum.InteractionTypeValue, 1)
    CALLS = typing___cast(InteractionTypeEnum.InteractionTypeValue, 8000)
    type___InteractionType = InteractionType
    def __init__(self,) -> None: ...

type___InteractionTypeEnum = InteractionTypeEnum

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

class CollectionSizeErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CollectionSizeErrorValue = typing___NewType(
        "CollectionSizeErrorValue", builtin___int
    )
    type___CollectionSizeErrorValue = CollectionSizeErrorValue
    CollectionSizeError: _CollectionSizeError
    class _CollectionSizeError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CollectionSizeErrorEnum.CollectionSizeErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 0)
        UNKNOWN = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 1)
        TOO_FEW = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 2)
        TOO_MANY = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 3)
    UNSPECIFIED = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 0)
    UNKNOWN = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 1)
    TOO_FEW = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 2)
    TOO_MANY = typing___cast(CollectionSizeErrorEnum.CollectionSizeErrorValue, 3)
    type___CollectionSizeError = CollectionSizeError
    def __init__(self,) -> None: ...

type___CollectionSizeErrorEnum = CollectionSizeErrorEnum

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

class ListOperationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ListOperationErrorValue = typing___NewType("ListOperationErrorValue", builtin___int)
    type___ListOperationErrorValue = ListOperationErrorValue
    ListOperationError: _ListOperationError
    class _ListOperationError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ListOperationErrorEnum.ListOperationErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ListOperationErrorEnum.ListOperationErrorValue, 0)
        UNKNOWN = typing___cast(ListOperationErrorEnum.ListOperationErrorValue, 1)
        REQUIRED_FIELD_MISSING = typing___cast(
            ListOperationErrorEnum.ListOperationErrorValue, 7
        )
        DUPLICATE_VALUES = typing___cast(
            ListOperationErrorEnum.ListOperationErrorValue, 8
        )
    UNSPECIFIED = typing___cast(ListOperationErrorEnum.ListOperationErrorValue, 0)
    UNKNOWN = typing___cast(ListOperationErrorEnum.ListOperationErrorValue, 1)
    REQUIRED_FIELD_MISSING = typing___cast(
        ListOperationErrorEnum.ListOperationErrorValue, 7
    )
    DUPLICATE_VALUES = typing___cast(ListOperationErrorEnum.ListOperationErrorValue, 8)
    type___ListOperationError = ListOperationError
    def __init__(self,) -> None: ...

type___ListOperationErrorEnum = ListOperationErrorEnum

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

class InternalErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    InternalErrorValue = typing___NewType("InternalErrorValue", builtin___int)
    type___InternalErrorValue = InternalErrorValue
    InternalError: _InternalError
    class _InternalError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            InternalErrorEnum.InternalErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(InternalErrorEnum.InternalErrorValue, 0)
        UNKNOWN = typing___cast(InternalErrorEnum.InternalErrorValue, 1)
        INTERNAL_ERROR = typing___cast(InternalErrorEnum.InternalErrorValue, 2)
        ERROR_CODE_NOT_PUBLISHED = typing___cast(
            InternalErrorEnum.InternalErrorValue, 3
        )
        TRANSIENT_ERROR = typing___cast(InternalErrorEnum.InternalErrorValue, 4)
        DEADLINE_EXCEEDED = typing___cast(InternalErrorEnum.InternalErrorValue, 5)
    UNSPECIFIED = typing___cast(InternalErrorEnum.InternalErrorValue, 0)
    UNKNOWN = typing___cast(InternalErrorEnum.InternalErrorValue, 1)
    INTERNAL_ERROR = typing___cast(InternalErrorEnum.InternalErrorValue, 2)
    ERROR_CODE_NOT_PUBLISHED = typing___cast(InternalErrorEnum.InternalErrorValue, 3)
    TRANSIENT_ERROR = typing___cast(InternalErrorEnum.InternalErrorValue, 4)
    DEADLINE_EXCEEDED = typing___cast(InternalErrorEnum.InternalErrorValue, 5)
    type___InternalError = InternalError
    def __init__(self,) -> None: ...

type___InternalErrorEnum = InternalErrorEnum

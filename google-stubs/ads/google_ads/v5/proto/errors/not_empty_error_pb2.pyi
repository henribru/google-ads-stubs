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

class NotEmptyErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    NotEmptyErrorValue = typing___NewType("NotEmptyErrorValue", builtin___int)
    type___NotEmptyErrorValue = NotEmptyErrorValue
    NotEmptyError: _NotEmptyError
    class _NotEmptyError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            NotEmptyErrorEnum.NotEmptyErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 0)
        UNKNOWN = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 1)
        EMPTY_LIST = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 2)
    UNSPECIFIED = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 0)
    UNKNOWN = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 1)
    EMPTY_LIST = typing___cast(NotEmptyErrorEnum.NotEmptyErrorValue, 2)
    type___NotEmptyError = NotEmptyError
    def __init__(self,) -> None: ...

type___NotEmptyErrorEnum = NotEmptyErrorEnum

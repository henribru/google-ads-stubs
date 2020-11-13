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

class ChangeEventErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ChangeEventErrorValue = typing___NewType("ChangeEventErrorValue", builtin___int)
    type___ChangeEventErrorValue = ChangeEventErrorValue
    ChangeEventError: _ChangeEventError
    class _ChangeEventError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ChangeEventErrorEnum.ChangeEventErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 0)
        UNKNOWN = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 1)
        START_DATE_TOO_OLD = typing___cast(
            ChangeEventErrorEnum.ChangeEventErrorValue, 2
        )
        CHANGE_DATE_RANGE_INFINITE = typing___cast(
            ChangeEventErrorEnum.ChangeEventErrorValue, 3
        )
        CHANGE_DATE_RANGE_NEGATIVE = typing___cast(
            ChangeEventErrorEnum.ChangeEventErrorValue, 4
        )
        LIMIT_NOT_SPECIFIED = typing___cast(
            ChangeEventErrorEnum.ChangeEventErrorValue, 5
        )
        INVALID_LIMIT_CLAUSE = typing___cast(
            ChangeEventErrorEnum.ChangeEventErrorValue, 6
        )
    UNSPECIFIED = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 0)
    UNKNOWN = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 1)
    START_DATE_TOO_OLD = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 2)
    CHANGE_DATE_RANGE_INFINITE = typing___cast(
        ChangeEventErrorEnum.ChangeEventErrorValue, 3
    )
    CHANGE_DATE_RANGE_NEGATIVE = typing___cast(
        ChangeEventErrorEnum.ChangeEventErrorValue, 4
    )
    LIMIT_NOT_SPECIFIED = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 5)
    INVALID_LIMIT_CLAUSE = typing___cast(ChangeEventErrorEnum.ChangeEventErrorValue, 6)
    type___ChangeEventError = ChangeEventError
    def __init__(self,) -> None: ...

type___ChangeEventErrorEnum = ChangeEventErrorEnum

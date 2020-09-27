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

class DatabaseErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DatabaseErrorValue = typing___NewType("DatabaseErrorValue", builtin___int)
    type___DatabaseErrorValue = DatabaseErrorValue
    DatabaseError: _DatabaseError
    class _DatabaseError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            DatabaseErrorEnum.DatabaseErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 0)
        UNKNOWN = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 1)
        CONCURRENT_MODIFICATION = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 2)
        DATA_CONSTRAINT_VIOLATION = typing___cast(
            DatabaseErrorEnum.DatabaseErrorValue, 3
        )
    UNSPECIFIED = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 0)
    UNKNOWN = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 1)
    CONCURRENT_MODIFICATION = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 2)
    DATA_CONSTRAINT_VIOLATION = typing___cast(DatabaseErrorEnum.DatabaseErrorValue, 3)
    type___DatabaseError = DatabaseError
    def __init__(self,) -> None: ...

type___DatabaseErrorEnum = DatabaseErrorEnum

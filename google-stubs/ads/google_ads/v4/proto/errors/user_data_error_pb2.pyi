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

class UserDataErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UserDataErrorValue = typing___NewType("UserDataErrorValue", builtin___int)
    type___UserDataErrorValue = UserDataErrorValue
    UserDataError: _UserDataError
    class _UserDataError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UserDataErrorEnum.UserDataErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(UserDataErrorEnum.UserDataErrorValue, 0)
        UNKNOWN = typing___cast(UserDataErrorEnum.UserDataErrorValue, 1)
        OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED = typing___cast(
            UserDataErrorEnum.UserDataErrorValue, 2
        )
        TOO_MANY_USER_IDENTIFIERS = typing___cast(
            UserDataErrorEnum.UserDataErrorValue, 3
        )
        USER_LIST_NOT_APPLICABLE = typing___cast(
            UserDataErrorEnum.UserDataErrorValue, 4
        )
    UNSPECIFIED = typing___cast(UserDataErrorEnum.UserDataErrorValue, 0)
    UNKNOWN = typing___cast(UserDataErrorEnum.UserDataErrorValue, 1)
    OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED = typing___cast(
        UserDataErrorEnum.UserDataErrorValue, 2
    )
    TOO_MANY_USER_IDENTIFIERS = typing___cast(UserDataErrorEnum.UserDataErrorValue, 3)
    USER_LIST_NOT_APPLICABLE = typing___cast(UserDataErrorEnum.UserDataErrorValue, 4)
    type___UserDataError = UserDataError
    def __init__(self,) -> None: ...

type___UserDataErrorEnum = UserDataErrorEnum

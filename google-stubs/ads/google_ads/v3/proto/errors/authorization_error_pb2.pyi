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

class AuthorizationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AuthorizationErrorValue = typing___NewType("AuthorizationErrorValue", builtin___int)
    type___AuthorizationErrorValue = AuthorizationErrorValue
    AuthorizationError: _AuthorizationError
    class _AuthorizationError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AuthorizationErrorEnum.AuthorizationErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 0)
        UNKNOWN = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 1)
        USER_PERMISSION_DENIED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 2
        )
        DEVELOPER_TOKEN_NOT_WHITELISTED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 3
        )
        DEVELOPER_TOKEN_PROHIBITED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 4
        )
        PROJECT_DISABLED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 5
        )
        AUTHORIZATION_ERROR = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 6
        )
        ACTION_NOT_PERMITTED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 7
        )
        INCOMPLETE_SIGNUP = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 8
        )
        CUSTOMER_NOT_ENABLED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 24
        )
        MISSING_TOS = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 9)
        DEVELOPER_TOKEN_NOT_APPROVED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 10
        )
        INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 11
        )
        SERVICE_ACCESS_DENIED = typing___cast(
            AuthorizationErrorEnum.AuthorizationErrorValue, 12
        )
    UNSPECIFIED = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 0)
    UNKNOWN = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 1)
    USER_PERMISSION_DENIED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 2
    )
    DEVELOPER_TOKEN_NOT_WHITELISTED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 3
    )
    DEVELOPER_TOKEN_PROHIBITED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 4
    )
    PROJECT_DISABLED = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 5)
    AUTHORIZATION_ERROR = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 6
    )
    ACTION_NOT_PERMITTED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 7
    )
    INCOMPLETE_SIGNUP = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 8)
    CUSTOMER_NOT_ENABLED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 24
    )
    MISSING_TOS = typing___cast(AuthorizationErrorEnum.AuthorizationErrorValue, 9)
    DEVELOPER_TOKEN_NOT_APPROVED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 10
    )
    INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 11
    )
    SERVICE_ACCESS_DENIED = typing___cast(
        AuthorizationErrorEnum.AuthorizationErrorValue, 12
    )
    type___AuthorizationError = AuthorizationError
    def __init__(self,) -> None: ...

type___AuthorizationErrorEnum = AuthorizationErrorEnum

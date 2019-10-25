# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class RequestErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class RequestError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> RequestErrorEnum.RequestError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[RequestErrorEnum.RequestError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, RequestErrorEnum.RequestError]]: ...
        UNSPECIFIED = typing___cast(RequestErrorEnum.RequestError, 0)
        UNKNOWN = typing___cast(RequestErrorEnum.RequestError, 1)
        RESOURCE_NAME_MISSING = typing___cast(RequestErrorEnum.RequestError, 3)
        RESOURCE_NAME_MALFORMED = typing___cast(RequestErrorEnum.RequestError, 4)
        BAD_RESOURCE_ID = typing___cast(RequestErrorEnum.RequestError, 17)
        INVALID_CUSTOMER_ID = typing___cast(RequestErrorEnum.RequestError, 16)
        OPERATION_REQUIRED = typing___cast(RequestErrorEnum.RequestError, 5)
        RESOURCE_NOT_FOUND = typing___cast(RequestErrorEnum.RequestError, 6)
        INVALID_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 7)
        EXPIRED_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 8)
        INVALID_PAGE_SIZE = typing___cast(RequestErrorEnum.RequestError, 22)
        REQUIRED_FIELD_MISSING = typing___cast(RequestErrorEnum.RequestError, 9)
        IMMUTABLE_FIELD = typing___cast(RequestErrorEnum.RequestError, 11)
        TOO_MANY_MUTATE_OPERATIONS = typing___cast(RequestErrorEnum.RequestError, 13)
        CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = typing___cast(RequestErrorEnum.RequestError, 14)
        CANNOT_MODIFY_FOREIGN_FIELD = typing___cast(RequestErrorEnum.RequestError, 15)
        INVALID_ENUM_VALUE = typing___cast(RequestErrorEnum.RequestError, 18)
        DEVELOPER_TOKEN_PARAMETER_MISSING = typing___cast(RequestErrorEnum.RequestError, 19)
        LOGIN_CUSTOMER_ID_PARAMETER_MISSING = typing___cast(RequestErrorEnum.RequestError, 20)
        VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 21)
    UNSPECIFIED = typing___cast(RequestErrorEnum.RequestError, 0)
    UNKNOWN = typing___cast(RequestErrorEnum.RequestError, 1)
    RESOURCE_NAME_MISSING = typing___cast(RequestErrorEnum.RequestError, 3)
    RESOURCE_NAME_MALFORMED = typing___cast(RequestErrorEnum.RequestError, 4)
    BAD_RESOURCE_ID = typing___cast(RequestErrorEnum.RequestError, 17)
    INVALID_CUSTOMER_ID = typing___cast(RequestErrorEnum.RequestError, 16)
    OPERATION_REQUIRED = typing___cast(RequestErrorEnum.RequestError, 5)
    RESOURCE_NOT_FOUND = typing___cast(RequestErrorEnum.RequestError, 6)
    INVALID_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 7)
    EXPIRED_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 8)
    INVALID_PAGE_SIZE = typing___cast(RequestErrorEnum.RequestError, 22)
    REQUIRED_FIELD_MISSING = typing___cast(RequestErrorEnum.RequestError, 9)
    IMMUTABLE_FIELD = typing___cast(RequestErrorEnum.RequestError, 11)
    TOO_MANY_MUTATE_OPERATIONS = typing___cast(RequestErrorEnum.RequestError, 13)
    CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = typing___cast(RequestErrorEnum.RequestError, 14)
    CANNOT_MODIFY_FOREIGN_FIELD = typing___cast(RequestErrorEnum.RequestError, 15)
    INVALID_ENUM_VALUE = typing___cast(RequestErrorEnum.RequestError, 18)
    DEVELOPER_TOKEN_PARAMETER_MISSING = typing___cast(RequestErrorEnum.RequestError, 19)
    LOGIN_CUSTOMER_ID_PARAMETER_MISSING = typing___cast(RequestErrorEnum.RequestError, 20)
    VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestError, 21)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RequestErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

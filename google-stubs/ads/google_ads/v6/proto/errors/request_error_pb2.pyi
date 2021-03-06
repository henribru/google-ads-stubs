"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RequestErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _RequestError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RequestError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = RequestErrorEnum.RequestError.V(0)
        UNKNOWN = RequestErrorEnum.RequestError.V(1)
        RESOURCE_NAME_MISSING = RequestErrorEnum.RequestError.V(3)
        RESOURCE_NAME_MALFORMED = RequestErrorEnum.RequestError.V(4)
        BAD_RESOURCE_ID = RequestErrorEnum.RequestError.V(17)
        INVALID_CUSTOMER_ID = RequestErrorEnum.RequestError.V(16)
        OPERATION_REQUIRED = RequestErrorEnum.RequestError.V(5)
        RESOURCE_NOT_FOUND = RequestErrorEnum.RequestError.V(6)
        INVALID_PAGE_TOKEN = RequestErrorEnum.RequestError.V(7)
        EXPIRED_PAGE_TOKEN = RequestErrorEnum.RequestError.V(8)
        INVALID_PAGE_SIZE = RequestErrorEnum.RequestError.V(22)
        REQUIRED_FIELD_MISSING = RequestErrorEnum.RequestError.V(9)
        IMMUTABLE_FIELD = RequestErrorEnum.RequestError.V(11)
        TOO_MANY_MUTATE_OPERATIONS = RequestErrorEnum.RequestError.V(13)
        CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = RequestErrorEnum.RequestError.V(14)
        CANNOT_MODIFY_FOREIGN_FIELD = RequestErrorEnum.RequestError.V(15)
        INVALID_ENUM_VALUE = RequestErrorEnum.RequestError.V(18)
        DEVELOPER_TOKEN_PARAMETER_MISSING = RequestErrorEnum.RequestError.V(19)
        LOGIN_CUSTOMER_ID_PARAMETER_MISSING = RequestErrorEnum.RequestError.V(20)
        VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = RequestErrorEnum.RequestError.V(21)
        CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS = (
            RequestErrorEnum.RequestError.V(29)
        )
        CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS = (
            RequestErrorEnum.RequestError.V(30)
        )
        INCONSISTENT_RETURN_SUMMARY_ROW_VALUE = RequestErrorEnum.RequestError.V(31)
        TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED = RequestErrorEnum.RequestError.V(
            32
        )
        RPC_DEADLINE_TOO_SHORT = RequestErrorEnum.RequestError.V(33)
    class RequestError(metaclass=_RequestError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = RequestErrorEnum.RequestError.V(0)
    UNKNOWN = RequestErrorEnum.RequestError.V(1)
    RESOURCE_NAME_MISSING = RequestErrorEnum.RequestError.V(3)
    RESOURCE_NAME_MALFORMED = RequestErrorEnum.RequestError.V(4)
    BAD_RESOURCE_ID = RequestErrorEnum.RequestError.V(17)
    INVALID_CUSTOMER_ID = RequestErrorEnum.RequestError.V(16)
    OPERATION_REQUIRED = RequestErrorEnum.RequestError.V(5)
    RESOURCE_NOT_FOUND = RequestErrorEnum.RequestError.V(6)
    INVALID_PAGE_TOKEN = RequestErrorEnum.RequestError.V(7)
    EXPIRED_PAGE_TOKEN = RequestErrorEnum.RequestError.V(8)
    INVALID_PAGE_SIZE = RequestErrorEnum.RequestError.V(22)
    REQUIRED_FIELD_MISSING = RequestErrorEnum.RequestError.V(9)
    IMMUTABLE_FIELD = RequestErrorEnum.RequestError.V(11)
    TOO_MANY_MUTATE_OPERATIONS = RequestErrorEnum.RequestError.V(13)
    CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = RequestErrorEnum.RequestError.V(14)
    CANNOT_MODIFY_FOREIGN_FIELD = RequestErrorEnum.RequestError.V(15)
    INVALID_ENUM_VALUE = RequestErrorEnum.RequestError.V(18)
    DEVELOPER_TOKEN_PARAMETER_MISSING = RequestErrorEnum.RequestError.V(19)
    LOGIN_CUSTOMER_ID_PARAMETER_MISSING = RequestErrorEnum.RequestError.V(20)
    VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = RequestErrorEnum.RequestError.V(21)
    CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS = (
        RequestErrorEnum.RequestError.V(29)
    )
    CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS = (
        RequestErrorEnum.RequestError.V(30)
    )
    INCONSISTENT_RETURN_SUMMARY_ROW_VALUE = RequestErrorEnum.RequestError.V(31)
    TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED = RequestErrorEnum.RequestError.V(32)
    RPC_DEADLINE_TOO_SHORT = RequestErrorEnum.RequestError.V(33)
    def __init__(
        self,
    ) -> None: ...

global___RequestErrorEnum = RequestErrorEnum

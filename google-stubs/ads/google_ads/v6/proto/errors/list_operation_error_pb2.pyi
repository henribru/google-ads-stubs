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

class ListOperationErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ListOperationError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ListOperationError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = ListOperationErrorEnum.ListOperationError.V(0)
        UNKNOWN = ListOperationErrorEnum.ListOperationError.V(1)
        REQUIRED_FIELD_MISSING = ListOperationErrorEnum.ListOperationError.V(7)
        DUPLICATE_VALUES = ListOperationErrorEnum.ListOperationError.V(8)
    class ListOperationError(metaclass=_ListOperationError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = ListOperationErrorEnum.ListOperationError.V(0)
    UNKNOWN = ListOperationErrorEnum.ListOperationError.V(1)
    REQUIRED_FIELD_MISSING = ListOperationErrorEnum.ListOperationError.V(7)
    DUPLICATE_VALUES = ListOperationErrorEnum.ListOperationError.V(8)
    def __init__(
        self,
    ) -> None: ...

global___ListOperationErrorEnum = ListOperationErrorEnum

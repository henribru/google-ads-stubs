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

class OperatorErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _OperatorError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[OperatorError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = OperatorErrorEnum.OperatorError.V(0)
        UNKNOWN = OperatorErrorEnum.OperatorError.V(1)
        OPERATOR_NOT_SUPPORTED = OperatorErrorEnum.OperatorError.V(2)
    class OperatorError(metaclass=_OperatorError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = OperatorErrorEnum.OperatorError.V(0)
    UNKNOWN = OperatorErrorEnum.OperatorError.V(1)
    OPERATOR_NOT_SUPPORTED = OperatorErrorEnum.OperatorError.V(2)
    def __init__(
        self,
    ) -> None: ...

global___OperatorErrorEnum = OperatorErrorEnum

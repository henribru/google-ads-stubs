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

class LinkedAccountTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _LinkedAccountType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            LinkedAccountType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = LinkedAccountTypeEnum.LinkedAccountType.V(0)
        UNKNOWN = LinkedAccountTypeEnum.LinkedAccountType.V(1)
        THIRD_PARTY_APP_ANALYTICS = LinkedAccountTypeEnum.LinkedAccountType.V(2)
    class LinkedAccountType(metaclass=_LinkedAccountType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = LinkedAccountTypeEnum.LinkedAccountType.V(0)
    UNKNOWN = LinkedAccountTypeEnum.LinkedAccountType.V(1)
    THIRD_PARTY_APP_ANALYTICS = LinkedAccountTypeEnum.LinkedAccountType.V(2)
    def __init__(
        self,
    ) -> None: ...

global___LinkedAccountTypeEnum = LinkedAccountTypeEnum

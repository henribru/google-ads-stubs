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

class AssetLinkErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AssetLinkError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AssetLinkError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AssetLinkErrorEnum.AssetLinkError.V(0)
        UNKNOWN = AssetLinkErrorEnum.AssetLinkError.V(1)
        PINNING_UNSUPPORTED = AssetLinkErrorEnum.AssetLinkError.V(2)
    class AssetLinkError(metaclass=_AssetLinkError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AssetLinkErrorEnum.AssetLinkError.V(0)
    UNKNOWN = AssetLinkErrorEnum.AssetLinkError.V(1)
    PINNING_UNSUPPORTED = AssetLinkErrorEnum.AssetLinkError.V(2)
    def __init__(
        self,
    ) -> None: ...

global___AssetLinkErrorEnum = AssetLinkErrorEnum

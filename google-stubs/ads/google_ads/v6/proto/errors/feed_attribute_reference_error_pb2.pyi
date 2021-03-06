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

class FeedAttributeReferenceErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FeedAttributeReferenceError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            FeedAttributeReferenceError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(0)
        UNKNOWN = FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(1)
        CANNOT_REFERENCE_REMOVED_FEED = (
            FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(2)
        )
        INVALID_FEED_NAME = (
            FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(3)
        )
        INVALID_FEED_ATTRIBUTE_NAME = (
            FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(4)
        )
    class FeedAttributeReferenceError(metaclass=_FeedAttributeReferenceError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(0)
    UNKNOWN = FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(1)
    CANNOT_REFERENCE_REMOVED_FEED = (
        FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(2)
    )
    INVALID_FEED_NAME = FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(3)
    INVALID_FEED_ATTRIBUTE_NAME = (
        FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError.V(4)
    )
    def __init__(
        self,
    ) -> None: ...

global___FeedAttributeReferenceErrorEnum = FeedAttributeReferenceErrorEnum

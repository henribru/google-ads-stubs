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

class StructuredSnippetPlaceholderFieldEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _StructuredSnippetPlaceholderField(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            StructuredSnippetPlaceholderField.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = (
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(0)
        )
        UNKNOWN = (
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(1)
        )
        HEADER = (
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(2)
        )
        SNIPPETS = (
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(3)
        )
    class StructuredSnippetPlaceholderField(
        metaclass=_StructuredSnippetPlaceholderField
    ):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = (
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(0)
    )
    UNKNOWN = StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(
        1
    )
    HEADER = StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(
        2
    )
    SNIPPETS = (
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField.V(3)
    )
    def __init__(
        self,
    ) -> None: ...

global___StructuredSnippetPlaceholderFieldEnum = StructuredSnippetPlaceholderFieldEnum

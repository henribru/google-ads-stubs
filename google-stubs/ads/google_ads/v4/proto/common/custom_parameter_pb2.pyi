"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CustomParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def value(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        key: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        value: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
    ) -> None: ...

global___CustomParameter = CustomParameter

# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomParameter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def key(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def value(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        key: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        value: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["key", b"key", "value", b"value"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["key", b"key", "value", b"value"]
    ) -> None: ...

type___CustomParameter = CustomParameter

# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdParameter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def ad_group_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def parameter_index(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def insertion_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group_criterion: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        parameter_index: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        insertion_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_criterion",
            b"ad_group_criterion",
            "insertion_text",
            b"insertion_text",
            "parameter_index",
            b"parameter_index",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_criterion",
            b"ad_group_criterion",
            "insertion_text",
            b"insertion_text",
            "parameter_index",
            b"parameter_index",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___AdParameter = AdParameter

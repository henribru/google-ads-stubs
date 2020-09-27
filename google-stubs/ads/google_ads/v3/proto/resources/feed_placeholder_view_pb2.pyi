# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.enums.placeholder_type_pb2 import (
    PlaceholderTypeEnum as google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeedPlaceholderView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    placeholder_type: google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        placeholder_type: typing___Optional[
            google___ads___googleads___v3___enums___placeholder_type_pb2___PlaceholderTypeEnum.PlaceholderTypeValue
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "placeholder_type", b"placeholder_type", "resource_name", b"resource_name"
        ],
    ) -> None: ...

type___FeedPlaceholderView = FeedPlaceholderView

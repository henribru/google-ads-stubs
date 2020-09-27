# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

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

class CampaignLabel(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def label(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        label: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "campaign", b"campaign", "label", b"label"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign",
            b"campaign",
            "label",
            b"label",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___CampaignLabel = CampaignLabel

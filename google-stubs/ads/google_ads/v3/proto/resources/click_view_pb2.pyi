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

from google.ads.google_ads.v3.proto.common.click_location_pb2 import (
    ClickLocation as google___ads___googleads___v3___common___click_location_pb2___ClickLocation,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ClickView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def area_of_interest(
        self,
    ) -> google___ads___googleads___v3___common___click_location_pb2___ClickLocation: ...
    @property
    def location_of_presence(
        self,
    ) -> google___ads___googleads___v3___common___click_location_pb2___ClickLocation: ...
    @property
    def page_number(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def ad_group_ad(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        gclid: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        area_of_interest: typing___Optional[
            google___ads___googleads___v3___common___click_location_pb2___ClickLocation
        ] = None,
        location_of_presence: typing___Optional[
            google___ads___googleads___v3___common___click_location_pb2___ClickLocation
        ] = None,
        page_number: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        ad_group_ad: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_ad",
            b"ad_group_ad",
            "area_of_interest",
            b"area_of_interest",
            "gclid",
            b"gclid",
            "location_of_presence",
            b"location_of_presence",
            "page_number",
            b"page_number",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_ad",
            b"ad_group_ad",
            "area_of_interest",
            b"area_of_interest",
            "gclid",
            b"gclid",
            "location_of_presence",
            b"location_of_presence",
            "page_number",
            b"page_number",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___ClickView = ClickView
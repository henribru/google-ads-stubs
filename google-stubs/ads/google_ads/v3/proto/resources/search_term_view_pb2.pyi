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

from google.ads.google_ads.v3.proto.enums.search_term_targeting_status_pb2 import (
    SearchTermTargetingStatusEnum as google___ads___googleads___v3___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SearchTermView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v3___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum.SearchTermTargetingStatusValue = ...
    @property
    def search_term(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        search_term: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        ad_group: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v3___enums___search_term_targeting_status_pb2___SearchTermTargetingStatusEnum.SearchTermTargetingStatusValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group", b"ad_group", "search_term", b"search_term"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group",
            b"ad_group",
            "resource_name",
            b"resource_name",
            "search_term",
            b"search_term",
            "status",
            b"status",
        ],
    ) -> None: ...

type___SearchTermView = SearchTermView

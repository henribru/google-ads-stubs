# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.enums.keyword_match_type_pb2 import (
    KeywordMatchTypeEnum as google___ads___googleads___v4___enums___keyword_match_type_pb2___KeywordMatchTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class KeywordPlanCampaignKeyword(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    match_type: google___ads___googleads___v4___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchTypeValue = ...
    @property
    def keyword_plan_campaign(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def negative(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        keyword_plan_campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        text: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        match_type: typing___Optional[
            google___ads___googleads___v4___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchTypeValue
        ] = None,
        negative: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
            "negative",
            b"negative",
            "text",
            b"text",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
            "match_type",
            b"match_type",
            "negative",
            b"negative",
            "resource_name",
            b"resource_name",
            "text",
            b"text",
        ],
    ) -> None: ...

type___KeywordPlanCampaignKeyword = KeywordPlanCampaignKeyword

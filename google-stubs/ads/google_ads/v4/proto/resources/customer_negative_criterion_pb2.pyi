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
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.common.criteria_pb2 import (
    ContentLabelInfo as google___ads___googleads___v4___common___criteria_pb2___ContentLabelInfo,
    MobileAppCategoryInfo as google___ads___googleads___v4___common___criteria_pb2___MobileAppCategoryInfo,
    MobileApplicationInfo as google___ads___googleads___v4___common___criteria_pb2___MobileApplicationInfo,
    PlacementInfo as google___ads___googleads___v4___common___criteria_pb2___PlacementInfo,
    YouTubeChannelInfo as google___ads___googleads___v4___common___criteria_pb2___YouTubeChannelInfo,
    YouTubeVideoInfo as google___ads___googleads___v4___common___criteria_pb2___YouTubeVideoInfo,
)
from google.ads.google_ads.v4.proto.enums.criterion_type_pb2 import (
    CriterionTypeEnum as google___ads___googleads___v4___enums___criterion_type_pb2___CriterionTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomerNegativeCriterion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    type: google___ads___googleads___v4___enums___criterion_type_pb2___CriterionTypeEnum.CriterionTypeValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def content_label(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___ContentLabelInfo: ...
    @property
    def mobile_application(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___MobileApplicationInfo: ...
    @property
    def mobile_app_category(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___MobileAppCategoryInfo: ...
    @property
    def placement(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___PlacementInfo: ...
    @property
    def youtube_video(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___YouTubeVideoInfo: ...
    @property
    def youtube_channel(
        self,
    ) -> google___ads___googleads___v4___common___criteria_pb2___YouTubeChannelInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        type: typing___Optional[
            google___ads___googleads___v4___enums___criterion_type_pb2___CriterionTypeEnum.CriterionTypeValue
        ] = None,
        content_label: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___ContentLabelInfo
        ] = None,
        mobile_application: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___MobileApplicationInfo
        ] = None,
        mobile_app_category: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___MobileAppCategoryInfo
        ] = None,
        placement: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___PlacementInfo
        ] = None,
        youtube_video: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___YouTubeVideoInfo
        ] = None,
        youtube_channel: typing___Optional[
            google___ads___googleads___v4___common___criteria_pb2___YouTubeChannelInfo
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "content_label",
            b"content_label",
            "criterion",
            b"criterion",
            "id",
            b"id",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "placement",
            b"placement",
            "youtube_channel",
            b"youtube_channel",
            "youtube_video",
            b"youtube_video",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "content_label",
            b"content_label",
            "criterion",
            b"criterion",
            "id",
            b"id",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "placement",
            b"placement",
            "resource_name",
            b"resource_name",
            "type",
            b"type",
            "youtube_channel",
            b"youtube_channel",
            "youtube_video",
            b"youtube_video",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["criterion", b"criterion"]
    ) -> typing_extensions___Literal[
        "content_label",
        "mobile_application",
        "mobile_app_category",
        "placement",
        "youtube_video",
        "youtube_channel",
    ]: ...

type___CustomerNegativeCriterion = CustomerNegativeCriterion

# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.criteria_pb2 import (
    ContentLabelInfo as google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo,
    MobileAppCategoryInfo as google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo,
    MobileApplicationInfo as google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo,
    PlacementInfo as google___ads___googleads___v2___common___criteria_pb2___PlacementInfo,
    YouTubeChannelInfo as google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo,
    YouTubeVideoInfo as google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo,
)

from google.ads.google_ads.v2.proto.enums.criterion_type_pb2 import (
    CriterionTypeEnum as google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CustomerNegativeCriterion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text
    type = ... # type: google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def content_label(self) -> google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo: ...

    @property
    def mobile_application(self) -> google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo: ...

    @property
    def mobile_app_category(self) -> google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo: ...

    @property
    def placement(self) -> google___ads___googleads___v2___common___criteria_pb2___PlacementInfo: ...

    @property
    def youtube_video(self) -> google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo: ...

    @property
    def youtube_channel(self) -> google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        type : typing___Optional[google___ads___googleads___v2___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType] = None,
        content_label : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___ContentLabelInfo] = None,
        mobile_application : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___MobileApplicationInfo] = None,
        mobile_app_category : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___MobileAppCategoryInfo] = None,
        placement : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___PlacementInfo] = None,
        youtube_video : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___YouTubeVideoInfo] = None,
        youtube_channel : typing___Optional[google___ads___googleads___v2___common___criteria_pb2___YouTubeChannelInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomerNegativeCriterion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"content_label",u"criterion",u"id",u"mobile_app_category",u"mobile_application",u"placement",u"youtube_channel",u"youtube_video"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content_label",u"criterion",u"id",u"mobile_app_category",u"mobile_application",u"placement",u"resource_name",u"type",u"youtube_channel",u"youtube_video"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"content_label",b"content_label",u"criterion",b"criterion",u"id",b"id",u"mobile_app_category",b"mobile_app_category",u"mobile_application",b"mobile_application",u"placement",b"placement",u"youtube_channel",b"youtube_channel",u"youtube_video",b"youtube_video"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content_label",b"content_label",u"criterion",b"criterion",u"id",b"id",u"mobile_app_category",b"mobile_app_category",u"mobile_application",b"mobile_application",u"placement",b"placement",u"resource_name",b"resource_name",u"type",b"type",u"youtube_channel",b"youtube_channel",u"youtube_video",b"youtube_video"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"criterion",b"criterion"]) -> typing_extensions___Literal["content_label","mobile_application","mobile_app_category","placement","youtube_video","youtube_channel"]: ...

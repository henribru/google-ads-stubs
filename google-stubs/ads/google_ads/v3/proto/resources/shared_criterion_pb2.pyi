# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.common.criteria_pb2 import (
    KeywordInfo as google___ads___googleads___v3___common___criteria_pb2___KeywordInfo,
    MobileAppCategoryInfo as google___ads___googleads___v3___common___criteria_pb2___MobileAppCategoryInfo,
    MobileApplicationInfo as google___ads___googleads___v3___common___criteria_pb2___MobileApplicationInfo,
    PlacementInfo as google___ads___googleads___v3___common___criteria_pb2___PlacementInfo,
    YouTubeChannelInfo as google___ads___googleads___v3___common___criteria_pb2___YouTubeChannelInfo,
    YouTubeVideoInfo as google___ads___googleads___v3___common___criteria_pb2___YouTubeVideoInfo,
)

from google.ads.google_ads.v3.proto.enums.criterion_type_pb2 import (
    CriterionTypeEnum as google___ads___googleads___v3___enums___criterion_type_pb2___CriterionTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class SharedCriterion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    type = (
        ...
    )  # type: google___ads___googleads___v3___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
    @property
    def shared_set(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def keyword(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___KeywordInfo: ...
    @property
    def youtube_video(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___YouTubeVideoInfo: ...
    @property
    def youtube_channel(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___YouTubeChannelInfo: ...
    @property
    def placement(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___PlacementInfo: ...
    @property
    def mobile_app_category(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___MobileAppCategoryInfo: ...
    @property
    def mobile_application(
        self,
    ) -> google___ads___googleads___v3___common___criteria_pb2___MobileApplicationInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        shared_set: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v3___enums___criterion_type_pb2___CriterionTypeEnum.CriterionType
        ] = None,
        keyword: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___KeywordInfo
        ] = None,
        youtube_video: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___YouTubeVideoInfo
        ] = None,
        youtube_channel: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___YouTubeChannelInfo
        ] = None,
        placement: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___PlacementInfo
        ] = None,
        mobile_app_category: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___MobileAppCategoryInfo
        ] = None,
        mobile_application: typing___Optional[
            google___ads___googleads___v3___common___criteria_pb2___MobileApplicationInfo
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SharedCriterion: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> SharedCriterion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "keyword",
            b"keyword",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "placement",
            b"placement",
            "shared_set",
            b"shared_set",
            "youtube_channel",
            b"youtube_channel",
            "youtube_video",
            b"youtube_video",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "keyword",
            b"keyword",
            "mobile_app_category",
            b"mobile_app_category",
            "mobile_application",
            b"mobile_application",
            "placement",
            b"placement",
            "resource_name",
            b"resource_name",
            "shared_set",
            b"shared_set",
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
        "keyword",
        "youtube_video",
        "youtube_channel",
        "placement",
        "mobile_app_category",
        "mobile_application",
    ]: ...

global___SharedCriterion = SharedCriterion

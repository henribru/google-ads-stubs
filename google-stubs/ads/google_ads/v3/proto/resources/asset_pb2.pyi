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

from google.ads.google_ads.v3.proto.common.asset_types_pb2 import (
    ImageAsset as google___ads___googleads___v3___common___asset_types_pb2___ImageAsset,
    MediaBundleAsset as google___ads___googleads___v3___common___asset_types_pb2___MediaBundleAsset,
    TextAsset as google___ads___googleads___v3___common___asset_types_pb2___TextAsset,
    YoutubeVideoAsset as google___ads___googleads___v3___common___asset_types_pb2___YoutubeVideoAsset,
)
from google.ads.google_ads.v3.proto.enums.asset_type_pb2 import (
    AssetTypeEnum as google___ads___googleads___v3___enums___asset_type_pb2___AssetTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Asset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    type: google___ads___googleads___v3___enums___asset_type_pb2___AssetTypeEnum.AssetTypeValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def youtube_video_asset(
        self,
    ) -> google___ads___googleads___v3___common___asset_types_pb2___YoutubeVideoAsset: ...
    @property
    def media_bundle_asset(
        self,
    ) -> google___ads___googleads___v3___common___asset_types_pb2___MediaBundleAsset: ...
    @property
    def image_asset(
        self,
    ) -> google___ads___googleads___v3___common___asset_types_pb2___ImageAsset: ...
    @property
    def text_asset(
        self,
    ) -> google___ads___googleads___v3___common___asset_types_pb2___TextAsset: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type: typing___Optional[
            google___ads___googleads___v3___enums___asset_type_pb2___AssetTypeEnum.AssetTypeValue
        ] = None,
        youtube_video_asset: typing___Optional[
            google___ads___googleads___v3___common___asset_types_pb2___YoutubeVideoAsset
        ] = None,
        media_bundle_asset: typing___Optional[
            google___ads___googleads___v3___common___asset_types_pb2___MediaBundleAsset
        ] = None,
        image_asset: typing___Optional[
            google___ads___googleads___v3___common___asset_types_pb2___ImageAsset
        ] = None,
        text_asset: typing___Optional[
            google___ads___googleads___v3___common___asset_types_pb2___TextAsset
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "asset_data",
            b"asset_data",
            "id",
            b"id",
            "image_asset",
            b"image_asset",
            "media_bundle_asset",
            b"media_bundle_asset",
            "name",
            b"name",
            "text_asset",
            b"text_asset",
            "youtube_video_asset",
            b"youtube_video_asset",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "asset_data",
            b"asset_data",
            "id",
            b"id",
            "image_asset",
            b"image_asset",
            "media_bundle_asset",
            b"media_bundle_asset",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "text_asset",
            b"text_asset",
            "type",
            b"type",
            "youtube_video_asset",
            b"youtube_video_asset",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["asset_data", b"asset_data"]
    ) -> typing_extensions___Literal[
        "youtube_video_asset", "media_bundle_asset", "image_asset", "text_asset"
    ]: ...

type___Asset = Asset

# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.media_type_pb2 import (
    MediaTypeEnum as google___ads___googleads___v5___enums___media_type_pb2___MediaTypeEnum,
)
from google.ads.google_ads.v5.proto.enums.mime_type_pb2 import (
    MimeTypeEnum as google___ads___googleads___v5___enums___mime_type_pb2___MimeTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class MediaFile(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    type: google___ads___googleads___v5___enums___media_type_pb2___MediaTypeEnum.MediaTypeValue = ...
    mime_type: google___ads___googleads___v5___enums___mime_type_pb2___MimeTypeEnum.MimeTypeValue = ...
    source_url: typing___Text = ...
    name: typing___Text = ...
    file_size: builtin___int = ...
    @property
    def image(self) -> type___MediaImage: ...
    @property
    def media_bundle(self) -> type___MediaBundle: ...
    @property
    def audio(self) -> type___MediaAudio: ...
    @property
    def video(self) -> type___MediaVideo: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        type: typing___Optional[
            google___ads___googleads___v5___enums___media_type_pb2___MediaTypeEnum.MediaTypeValue
        ] = None,
        mime_type: typing___Optional[
            google___ads___googleads___v5___enums___mime_type_pb2___MimeTypeEnum.MimeTypeValue
        ] = None,
        source_url: typing___Optional[typing___Text] = None,
        name: typing___Optional[typing___Text] = None,
        file_size: typing___Optional[builtin___int] = None,
        image: typing___Optional[type___MediaImage] = None,
        media_bundle: typing___Optional[type___MediaBundle] = None,
        audio: typing___Optional[type___MediaAudio] = None,
        video: typing___Optional[type___MediaVideo] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_file_size",
            b"_file_size",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_source_url",
            b"_source_url",
            "audio",
            b"audio",
            "file_size",
            b"file_size",
            "id",
            b"id",
            "image",
            b"image",
            "media_bundle",
            b"media_bundle",
            "mediatype",
            b"mediatype",
            "name",
            b"name",
            "source_url",
            b"source_url",
            "video",
            b"video",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_file_size",
            b"_file_size",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_source_url",
            b"_source_url",
            "audio",
            b"audio",
            "file_size",
            b"file_size",
            "id",
            b"id",
            "image",
            b"image",
            "media_bundle",
            b"media_bundle",
            "mediatype",
            b"mediatype",
            "mime_type",
            b"mime_type",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "source_url",
            b"source_url",
            "type",
            b"type",
            "video",
            b"video",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_file_size", b"_file_size"]
    ) -> typing_extensions___Literal["file_size"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_source_url", b"_source_url"]
    ) -> typing_extensions___Literal["source_url"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["mediatype", b"mediatype"]
    ) -> typing_extensions___Literal["image", "media_bundle", "audio", "video"]: ...

type___MediaFile = MediaFile

class MediaImage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    data: builtin___bytes = ...
    full_size_image_url: typing___Text = ...
    preview_size_image_url: typing___Text = ...
    def __init__(
        self,
        *,
        data: typing___Optional[builtin___bytes] = None,
        full_size_image_url: typing___Optional[typing___Text] = None,
        preview_size_image_url: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_data",
            b"_data",
            "_full_size_image_url",
            b"_full_size_image_url",
            "_preview_size_image_url",
            b"_preview_size_image_url",
            "data",
            b"data",
            "full_size_image_url",
            b"full_size_image_url",
            "preview_size_image_url",
            b"preview_size_image_url",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_data",
            b"_data",
            "_full_size_image_url",
            b"_full_size_image_url",
            "_preview_size_image_url",
            b"_preview_size_image_url",
            "data",
            b"data",
            "full_size_image_url",
            b"full_size_image_url",
            "preview_size_image_url",
            b"preview_size_image_url",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_data", b"_data"]
    ) -> typing_extensions___Literal["data"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_full_size_image_url", b"_full_size_image_url"
        ],
    ) -> typing_extensions___Literal["full_size_image_url"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_preview_size_image_url", b"_preview_size_image_url"
        ],
    ) -> typing_extensions___Literal["preview_size_image_url"]: ...

type___MediaImage = MediaImage

class MediaBundle(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    data: builtin___bytes = ...
    url: typing___Text = ...
    def __init__(
        self,
        *,
        data: typing___Optional[builtin___bytes] = None,
        url: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_data", b"_data", "_url", b"_url", "data", b"data", "url", b"url"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_data", b"_data", "_url", b"_url", "data", b"data", "url", b"url"
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_data", b"_data"]
    ) -> typing_extensions___Literal["data"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_url", b"_url"]
    ) -> typing_extensions___Literal["url"]: ...

type___MediaBundle = MediaBundle

class MediaAudio(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ad_duration_millis: builtin___int = ...
    def __init__(
        self, *, ad_duration_millis: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_duration_millis",
            b"_ad_duration_millis",
            "ad_duration_millis",
            b"ad_duration_millis",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_duration_millis",
            b"_ad_duration_millis",
            "ad_duration_millis",
            b"ad_duration_millis",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_ad_duration_millis", b"_ad_duration_millis"
        ],
    ) -> typing_extensions___Literal["ad_duration_millis"]: ...

type___MediaAudio = MediaAudio

class MediaVideo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ad_duration_millis: builtin___int = ...
    youtube_video_id: typing___Text = ...
    advertising_id_code: typing___Text = ...
    isci_code: typing___Text = ...
    def __init__(
        self,
        *,
        ad_duration_millis: typing___Optional[builtin___int] = None,
        youtube_video_id: typing___Optional[typing___Text] = None,
        advertising_id_code: typing___Optional[typing___Text] = None,
        isci_code: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_duration_millis",
            b"_ad_duration_millis",
            "_advertising_id_code",
            b"_advertising_id_code",
            "_isci_code",
            b"_isci_code",
            "_youtube_video_id",
            b"_youtube_video_id",
            "ad_duration_millis",
            b"ad_duration_millis",
            "advertising_id_code",
            b"advertising_id_code",
            "isci_code",
            b"isci_code",
            "youtube_video_id",
            b"youtube_video_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_duration_millis",
            b"_ad_duration_millis",
            "_advertising_id_code",
            b"_advertising_id_code",
            "_isci_code",
            b"_isci_code",
            "_youtube_video_id",
            b"_youtube_video_id",
            "ad_duration_millis",
            b"ad_duration_millis",
            "advertising_id_code",
            b"advertising_id_code",
            "isci_code",
            b"isci_code",
            "youtube_video_id",
            b"youtube_video_id",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_ad_duration_millis", b"_ad_duration_millis"
        ],
    ) -> typing_extensions___Literal["ad_duration_millis"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_advertising_id_code", b"_advertising_id_code"
        ],
    ) -> typing_extensions___Literal["advertising_id_code"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_isci_code", b"_isci_code"]
    ) -> typing_extensions___Literal["isci_code"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_youtube_video_id", b"_youtube_video_id"
        ],
    ) -> typing_extensions___Literal["youtube_video_id"]: ...

type___MediaVideo = MediaVideo

from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.media_type import MediaTypeEnum
from google.ads.googleads.v15.enums.types.mime_type import MimeTypeEnum

_M = TypeVar("_M")

class MediaAudio(proto.Message):
    ad_duration_millis: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_duration_millis: int = ...
    ) -> None: ...

class MediaBundle(proto.Message):
    data: bytes
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data: bytes = ...,
        url: str = ...
    ) -> None: ...

class MediaFile(proto.Message):
    resource_name: str
    id: int
    type_: MediaTypeEnum.MediaType
    mime_type: MimeTypeEnum.MimeType
    source_url: str
    name: str
    file_size: int
    image: MediaImage
    media_bundle: MediaBundle
    audio: MediaAudio
    video: MediaVideo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        type_: MediaTypeEnum.MediaType = ...,
        mime_type: MimeTypeEnum.MimeType = ...,
        source_url: str = ...,
        name: str = ...,
        file_size: int = ...,
        image: MediaImage = ...,
        media_bundle: MediaBundle = ...,
        audio: MediaAudio = ...,
        video: MediaVideo = ...
    ) -> None: ...

class MediaImage(proto.Message):
    data: bytes
    full_size_image_url: str
    preview_size_image_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data: bytes = ...,
        full_size_image_url: str = ...,
        preview_size_image_url: str = ...
    ) -> None: ...

class MediaVideo(proto.Message):
    ad_duration_millis: int
    youtube_video_id: str
    advertising_id_code: str
    isci_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_duration_millis: int = ...,
        youtube_video_id: str = ...,
        advertising_id_code: str = ...,
        isci_code: str = ...
    ) -> None: ...

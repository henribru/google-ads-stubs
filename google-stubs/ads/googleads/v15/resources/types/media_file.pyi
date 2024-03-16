from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        ad_duration_millis: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_duration_millis"]
    ) -> bool: ...

class MediaBundle(proto.Message):
    data: bytes
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        data: bytes = ...,
        url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["data", "url"]
    ) -> bool: ...

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
        video: MediaVideo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "type_",
            "mime_type",
            "source_url",
            "name",
            "file_size",
            "image",
            "media_bundle",
            "audio",
            "video",
        ],
    ) -> bool: ...

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
        preview_size_image_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["data", "full_size_image_url", "preview_size_image_url"]
    ) -> bool: ...

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
        isci_code: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "ad_duration_millis", "youtube_video_id", "advertising_id_code", "isci_code"
        ],
    ) -> bool: ...

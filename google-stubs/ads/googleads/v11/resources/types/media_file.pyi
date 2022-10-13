from typing import Any

import proto

from google.ads.googleads.v11.enums.types.media_type import MediaTypeEnum
from google.ads.googleads.v11.enums.types.mime_type import MimeTypeEnum

class MediaAudio(proto.Message):
    ad_duration_millis: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_duration_millis: int = ...
    ) -> None: ...

class MediaBundle(proto.Message):
    data: bytes
    url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_duration_millis: int = ...,
        youtube_video_id: str = ...,
        advertising_id_code: str = ...,
        isci_code: str = ...
    ) -> None: ...

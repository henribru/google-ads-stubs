from typing import Any

import proto

from google.ads.googleads.v7.enums.types import media_type as media_type

__protobuf__: Any

class MediaFile(proto.Message):
    resource_name: Any
    id: Any
    type_: Any
    mime_type: Any
    source_url: Any
    name: Any
    file_size: Any
    image: Any
    media_bundle: Any
    audio: Any
    video: Any

class MediaImage(proto.Message):
    data: Any
    full_size_image_url: Any
    preview_size_image_url: Any

class MediaBundle(proto.Message):
    data: Any
    url: Any

class MediaAudio(proto.Message):
    ad_duration_millis: Any

class MediaVideo(proto.Message):
    ad_duration_millis: Any
    youtube_video_id: Any
    advertising_id_code: Any
    isci_code: Any

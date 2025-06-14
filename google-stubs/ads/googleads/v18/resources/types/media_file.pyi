import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import media_type, mime_type as gage_mime_type

__protobuf__: Incomplete

class MediaFile(proto.Message):
    resource_name: str
    id: int
    type_: media_type.MediaTypeEnum.MediaType
    mime_type: gage_mime_type.MimeTypeEnum.MimeType
    source_url: str
    name: str
    file_size: int
    image: MediaImage
    media_bundle: MediaBundle
    audio: MediaAudio
    video: MediaVideo

class MediaImage(proto.Message):
    data: bytes
    full_size_image_url: str
    preview_size_image_url: str

class MediaBundle(proto.Message):
    data: bytes
    url: str

class MediaAudio(proto.Message):
    ad_duration_millis: int

class MediaVideo(proto.Message):
    ad_duration_millis: int
    youtube_video_id: str
    advertising_id_code: str
    isci_code: str

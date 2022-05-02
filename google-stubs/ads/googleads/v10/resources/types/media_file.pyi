import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import media_type as media_type

__protobuf__: Incomplete

class MediaFile(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    type_: Incomplete
    mime_type: Incomplete
    source_url: Incomplete
    name: Incomplete
    file_size: Incomplete
    image: Incomplete
    media_bundle: Incomplete
    audio: Incomplete
    video: Incomplete

class MediaImage(proto.Message):
    data: Incomplete
    full_size_image_url: Incomplete
    preview_size_image_url: Incomplete

class MediaBundle(proto.Message):
    data: Incomplete
    url: Incomplete

class MediaAudio(proto.Message):
    ad_duration_millis: Incomplete

class MediaVideo(proto.Message):
    ad_duration_millis: Incomplete
    youtube_video_id: Incomplete
    advertising_id_code: Incomplete
    isci_code: Incomplete

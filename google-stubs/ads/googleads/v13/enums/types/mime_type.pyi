from typing import Any

import proto

class MimeTypeEnum(proto.Message):
    class MimeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IMAGE_JPEG = 2
        IMAGE_GIF = 3
        IMAGE_PNG = 4
        FLASH = 5
        TEXT_HTML = 6
        PDF = 7
        MSWORD = 8
        MSEXCEL = 9
        RTF = 10
        AUDIO_WAV = 11
        AUDIO_MP3 = 12
        HTML5_AD_ZIP = 13
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

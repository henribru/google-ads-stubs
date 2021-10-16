from typing import Any

import proto

__protobuf__: Any

class MimeTypeEnum(proto.Message):
    class MimeType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IMAGE_JPEG: int
        IMAGE_GIF: int
        IMAGE_PNG: int
        FLASH: int
        TEXT_HTML: int
        PDF: int
        MSWORD: int
        MSEXCEL: int
        RTF: int
        AUDIO_WAV: int
        AUDIO_MP3: int
        HTML5_AD_ZIP: int

from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MediaUploadErrorEnum(proto.Message):
    class MediaUploadError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FILE_TOO_BIG = 2
        UNPARSEABLE_IMAGE = 3
        ANIMATED_IMAGE_NOT_ALLOWED = 4
        FORMAT_NOT_ALLOWED = 5
        EXTERNAL_URL_NOT_ALLOWED = 6
        INVALID_URL_REFERENCE = 7
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = 8
        ANIMATED_VISUAL_EFFECT = 9
        ANIMATION_TOO_LONG = 10
        ASPECT_RATIO_NOT_ALLOWED = 11
        AUDIO_NOT_ALLOWED_IN_MEDIA_BUNDLE = 12
        CMYK_JPEG_NOT_ALLOWED = 13
        FLASH_NOT_ALLOWED = 14
        FRAME_RATE_TOO_HIGH = 15
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED = 16
        IMAGE_CONSTRAINTS_VIOLATED = 17
        INVALID_MEDIA_BUNDLE = 18
        INVALID_MEDIA_BUNDLE_ENTRY = 19
        INVALID_MIME_TYPE = 20
        INVALID_PATH = 21
        LAYOUT_PROBLEM = 22
        MALFORMED_URL = 23
        MEDIA_BUNDLE_NOT_ALLOWED = 24
        MEDIA_BUNDLE_NOT_COMPATIBLE_TO_PRODUCT_TYPE = 25
        MEDIA_BUNDLE_REJECTED_BY_MULTIPLE_ASSET_SPECS = 26
        TOO_MANY_FILES_IN_MEDIA_BUNDLE = 27
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT = 28
        UNSUPPORTED_HTML5_FEATURE = 29
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT = 30
        VIDEO_FILE_NAME_TOO_LONG = 31
        VIDEO_MULTIPLE_FILES_WITH_SAME_NAME = 32
        VIDEO_NOT_ALLOWED_IN_MEDIA_BUNDLE = 33
        CANNOT_UPLOAD_MEDIA_TYPE_THROUGH_API = 34
        DIMENSIONS_NOT_ALLOWED = 35

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

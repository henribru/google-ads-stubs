from typing import Any

import proto

__protobuf__: Any

class MediaBundleErrorEnum(proto.Message):
    class MediaBundleError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BAD_REQUEST: int
        DOUBLECLICK_BUNDLE_NOT_ALLOWED: int
        EXTERNAL_URL_NOT_ALLOWED: int
        FILE_TOO_LARGE: int
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: int
        INVALID_INPUT: int
        INVALID_MEDIA_BUNDLE: int
        INVALID_MEDIA_BUNDLE_ENTRY: int
        INVALID_MIME_TYPE: int
        INVALID_PATH: int
        INVALID_URL_REFERENCE: int
        MEDIA_DATA_TOO_LARGE: int
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: int
        SERVER_ERROR: int
        STORAGE_ERROR: int
        SWIFFY_BUNDLE_NOT_ALLOWED: int
        TOO_MANY_FILES: int
        UNEXPECTED_SIZE: int
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: int
        UNSUPPORTED_HTML5_FEATURE: int
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: int
        CUSTOM_EXIT_NOT_ALLOWED: int

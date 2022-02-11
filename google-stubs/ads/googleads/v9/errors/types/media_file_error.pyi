from typing import Any

import proto

__protobuf__: Any

class MediaFileErrorEnum(proto.Message):
    class MediaFileError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_CREATE_STANDARD_ICON: int
        CANNOT_SELECT_STANDARD_ICON_WITH_OTHER_TYPES: int
        CANNOT_SPECIFY_MEDIA_FILE_ID_AND_DATA: int
        DUPLICATE_MEDIA: int
        EMPTY_FIELD: int
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS: int
        FIELD_NOT_SUPPORTED_FOR_MEDIA_SUB_TYPE: int
        INVALID_MEDIA_FILE_ID: int
        INVALID_MEDIA_SUB_TYPE: int
        INVALID_MEDIA_FILE_TYPE: int
        INVALID_MIME_TYPE: int
        INVALID_REFERENCE_ID: int
        INVALID_YOU_TUBE_ID: int
        MEDIA_FILE_FAILED_TRANSCODING: int
        MEDIA_NOT_TRANSCODED: int
        MEDIA_TYPE_DOES_NOT_MATCH_MEDIA_FILE_TYPE: int
        NO_FIELDS_SPECIFIED: int
        NULL_REFERENCE_ID_AND_MEDIA_ID: int
        TOO_LONG: int
        UNSUPPORTED_TYPE: int
        YOU_TUBE_SERVICE_UNAVAILABLE: int
        YOU_TUBE_VIDEO_HAS_NON_POSITIVE_DURATION: int
        YOU_TUBE_VIDEO_NOT_FOUND: int

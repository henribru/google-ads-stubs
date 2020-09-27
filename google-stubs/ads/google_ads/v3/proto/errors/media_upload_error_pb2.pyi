# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class MediaUploadErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    MediaUploadErrorValue = typing___NewType("MediaUploadErrorValue", builtin___int)
    type___MediaUploadErrorValue = MediaUploadErrorValue
    MediaUploadError: _MediaUploadError
    class _MediaUploadError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            MediaUploadErrorEnum.MediaUploadErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 0)
        UNKNOWN = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 1)
        FILE_TOO_BIG = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 2)
        UNPARSEABLE_IMAGE = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 3)
        ANIMATED_IMAGE_NOT_ALLOWED = typing___cast(
            MediaUploadErrorEnum.MediaUploadErrorValue, 4
        )
        FORMAT_NOT_ALLOWED = typing___cast(
            MediaUploadErrorEnum.MediaUploadErrorValue, 5
        )
        EXTERNAL_URL_NOT_ALLOWED = typing___cast(
            MediaUploadErrorEnum.MediaUploadErrorValue, 6
        )
        INVALID_URL_REFERENCE = typing___cast(
            MediaUploadErrorEnum.MediaUploadErrorValue, 7
        )
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
            MediaUploadErrorEnum.MediaUploadErrorValue, 8
        )
    UNSPECIFIED = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 0)
    UNKNOWN = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 1)
    FILE_TOO_BIG = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 2)
    UNPARSEABLE_IMAGE = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 3)
    ANIMATED_IMAGE_NOT_ALLOWED = typing___cast(
        MediaUploadErrorEnum.MediaUploadErrorValue, 4
    )
    FORMAT_NOT_ALLOWED = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 5)
    EXTERNAL_URL_NOT_ALLOWED = typing___cast(
        MediaUploadErrorEnum.MediaUploadErrorValue, 6
    )
    INVALID_URL_REFERENCE = typing___cast(MediaUploadErrorEnum.MediaUploadErrorValue, 7)
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY = typing___cast(
        MediaUploadErrorEnum.MediaUploadErrorValue, 8
    )
    type___MediaUploadError = MediaUploadError
    def __init__(self,) -> None: ...

type___MediaUploadErrorEnum = MediaUploadErrorEnum

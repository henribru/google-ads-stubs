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

class YoutubeVideoRegistrationErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    YoutubeVideoRegistrationErrorValue = typing___NewType(
        "YoutubeVideoRegistrationErrorValue", builtin___int
    )
    type___YoutubeVideoRegistrationErrorValue = YoutubeVideoRegistrationErrorValue
    YoutubeVideoRegistrationError: _YoutubeVideoRegistrationError
    class _YoutubeVideoRegistrationError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 0
        )
        UNKNOWN = typing___cast(
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 1
        )
        VIDEO_NOT_FOUND = typing___cast(
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 2
        )
        VIDEO_NOT_ACCESSIBLE = typing___cast(
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 3
        )
        VIDEO_NOT_ELIGIBLE = typing___cast(
            YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 4
        )
    UNSPECIFIED = typing___cast(
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 0
    )
    UNKNOWN = typing___cast(
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 1
    )
    VIDEO_NOT_FOUND = typing___cast(
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 2
    )
    VIDEO_NOT_ACCESSIBLE = typing___cast(
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 3
    )
    VIDEO_NOT_ELIGIBLE = typing___cast(
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationErrorValue, 4
    )
    type___YoutubeVideoRegistrationError = YoutubeVideoRegistrationError
    def __init__(self,) -> None: ...

type___YoutubeVideoRegistrationErrorEnum = YoutubeVideoRegistrationErrorEnum

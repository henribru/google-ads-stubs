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

class FrequencyCapEventTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FrequencyCapEventTypeValue = typing___NewType(
        "FrequencyCapEventTypeValue", builtin___int
    )
    type___FrequencyCapEventTypeValue = FrequencyCapEventTypeValue
    FrequencyCapEventType: _FrequencyCapEventType
    class _FrequencyCapEventType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 0
        )
        UNKNOWN = typing___cast(FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 1)
        IMPRESSION = typing___cast(
            FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 2
        )
        VIDEO_VIEW = typing___cast(
            FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 3
        )
    UNSPECIFIED = typing___cast(FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 0)
    UNKNOWN = typing___cast(FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 1)
    IMPRESSION = typing___cast(FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 2)
    VIDEO_VIEW = typing___cast(FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue, 3)
    type___FrequencyCapEventType = FrequencyCapEventType
    def __init__(self,) -> None: ...

type___FrequencyCapEventTypeEnum = FrequencyCapEventTypeEnum

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

class SizeLimitErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SizeLimitErrorValue = typing___NewType("SizeLimitErrorValue", builtin___int)
    type___SizeLimitErrorValue = SizeLimitErrorValue
    SizeLimitError: _SizeLimitError
    class _SizeLimitError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SizeLimitErrorEnum.SizeLimitErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(SizeLimitErrorEnum.SizeLimitErrorValue, 0)
        UNKNOWN = typing___cast(SizeLimitErrorEnum.SizeLimitErrorValue, 1)
        REQUEST_SIZE_LIMIT_EXCEEDED = typing___cast(
            SizeLimitErrorEnum.SizeLimitErrorValue, 2
        )
        RESPONSE_SIZE_LIMIT_EXCEEDED = typing___cast(
            SizeLimitErrorEnum.SizeLimitErrorValue, 3
        )
    UNSPECIFIED = typing___cast(SizeLimitErrorEnum.SizeLimitErrorValue, 0)
    UNKNOWN = typing___cast(SizeLimitErrorEnum.SizeLimitErrorValue, 1)
    REQUEST_SIZE_LIMIT_EXCEEDED = typing___cast(
        SizeLimitErrorEnum.SizeLimitErrorValue, 2
    )
    RESPONSE_SIZE_LIMIT_EXCEEDED = typing___cast(
        SizeLimitErrorEnum.SizeLimitErrorValue, 3
    )
    type___SizeLimitError = SizeLimitError
    def __init__(self,) -> None: ...

type___SizeLimitErrorEnum = SizeLimitErrorEnum

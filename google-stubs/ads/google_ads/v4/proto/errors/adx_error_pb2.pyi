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

class AdxErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AdxErrorValue = typing___NewType("AdxErrorValue", builtin___int)
    type___AdxErrorValue = AdxErrorValue
    AdxError: _AdxError
    class _AdxError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AdxErrorEnum.AdxErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AdxErrorEnum.AdxErrorValue, 0)
        UNKNOWN = typing___cast(AdxErrorEnum.AdxErrorValue, 1)
        UNSUPPORTED_FEATURE = typing___cast(AdxErrorEnum.AdxErrorValue, 2)
    UNSPECIFIED = typing___cast(AdxErrorEnum.AdxErrorValue, 0)
    UNKNOWN = typing___cast(AdxErrorEnum.AdxErrorValue, 1)
    UNSUPPORTED_FEATURE = typing___cast(AdxErrorEnum.AdxErrorValue, 2)
    type___AdxError = AdxError
    def __init__(self,) -> None: ...

type___AdxErrorEnum = AdxErrorEnum

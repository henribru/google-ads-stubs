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

class SharedSetStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SharedSetStatusValue = typing___NewType("SharedSetStatusValue", builtin___int)
    type___SharedSetStatusValue = SharedSetStatusValue
    SharedSetStatus: _SharedSetStatus
    class _SharedSetStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SharedSetStatusEnum.SharedSetStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 0)
        UNKNOWN = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 1)
        ENABLED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 2)
        REMOVED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 3)
    UNSPECIFIED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 0)
    UNKNOWN = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 1)
    ENABLED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 2)
    REMOVED = typing___cast(SharedSetStatusEnum.SharedSetStatusValue, 3)
    type___SharedSetStatus = SharedSetStatus
    def __init__(self,) -> None: ...

type___SharedSetStatusEnum = SharedSetStatusEnum

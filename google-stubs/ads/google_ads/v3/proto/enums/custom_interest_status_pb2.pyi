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

class CustomInterestStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomInterestStatusValue = typing___NewType(
        "CustomInterestStatusValue", builtin___int
    )
    type___CustomInterestStatusValue = CustomInterestStatusValue
    CustomInterestStatus: _CustomInterestStatus
    class _CustomInterestStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomInterestStatusEnum.CustomInterestStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CustomInterestStatusEnum.CustomInterestStatusValue, 0
        )
        UNKNOWN = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 1)
        ENABLED = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 2)
        REMOVED = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 3)
    UNSPECIFIED = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 0)
    UNKNOWN = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 1)
    ENABLED = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 2)
    REMOVED = typing___cast(CustomInterestStatusEnum.CustomInterestStatusValue, 3)
    type___CustomInterestStatus = CustomInterestStatus
    def __init__(self,) -> None: ...

type___CustomInterestStatusEnum = CustomInterestStatusEnum
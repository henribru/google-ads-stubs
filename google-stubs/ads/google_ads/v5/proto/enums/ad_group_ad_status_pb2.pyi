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

class AdGroupAdStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AdGroupAdStatusValue = typing___NewType("AdGroupAdStatusValue", builtin___int)
    type___AdGroupAdStatusValue = AdGroupAdStatusValue
    AdGroupAdStatus: _AdGroupAdStatus
    class _AdGroupAdStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AdGroupAdStatusEnum.AdGroupAdStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 0)
        UNKNOWN = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 1)
        ENABLED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 2)
        PAUSED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 3)
        REMOVED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 4)
    UNSPECIFIED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 0)
    UNKNOWN = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 1)
    ENABLED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 2)
    PAUSED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 3)
    REMOVED = typing___cast(AdGroupAdStatusEnum.AdGroupAdStatusValue, 4)
    type___AdGroupAdStatus = AdGroupAdStatus
    def __init__(self,) -> None: ...

type___AdGroupAdStatusEnum = AdGroupAdStatusEnum

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

class FeedStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedStatusValue = typing___NewType("FeedStatusValue", builtin___int)
    type___FeedStatusValue = FeedStatusValue
    FeedStatus: _FeedStatus
    class _FeedStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedStatusEnum.FeedStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(FeedStatusEnum.FeedStatusValue, 0)
        UNKNOWN = typing___cast(FeedStatusEnum.FeedStatusValue, 1)
        ENABLED = typing___cast(FeedStatusEnum.FeedStatusValue, 2)
        REMOVED = typing___cast(FeedStatusEnum.FeedStatusValue, 3)
    UNSPECIFIED = typing___cast(FeedStatusEnum.FeedStatusValue, 0)
    UNKNOWN = typing___cast(FeedStatusEnum.FeedStatusValue, 1)
    ENABLED = typing___cast(FeedStatusEnum.FeedStatusValue, 2)
    REMOVED = typing___cast(FeedStatusEnum.FeedStatusValue, 3)
    type___FeedStatus = FeedStatus
    def __init__(self,) -> None: ...

type___FeedStatusEnum = FeedStatusEnum
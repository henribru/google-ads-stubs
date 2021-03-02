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

class FeedItemSetErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemSetErrorValue = typing___NewType("FeedItemSetErrorValue", builtin___int)
    type___FeedItemSetErrorValue = FeedItemSetErrorValue
    FeedItemSetError: _FeedItemSetError
    class _FeedItemSetError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemSetErrorEnum.FeedItemSetErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 0)
        UNKNOWN = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 1)
        FEED_ITEM_SET_REMOVED = typing___cast(
            FeedItemSetErrorEnum.FeedItemSetErrorValue, 2
        )
        CANNOT_CLEAR_DYNAMIC_FILTER = typing___cast(
            FeedItemSetErrorEnum.FeedItemSetErrorValue, 3
        )
        CANNOT_CREATE_DYNAMIC_FILTER = typing___cast(
            FeedItemSetErrorEnum.FeedItemSetErrorValue, 4
        )
        INVALID_FEED_TYPE = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 5)
        DUPLICATE_NAME = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 6)
        WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE = typing___cast(
            FeedItemSetErrorEnum.FeedItemSetErrorValue, 7
        )
    UNSPECIFIED = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 0)
    UNKNOWN = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 1)
    FEED_ITEM_SET_REMOVED = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 2)
    CANNOT_CLEAR_DYNAMIC_FILTER = typing___cast(
        FeedItemSetErrorEnum.FeedItemSetErrorValue, 3
    )
    CANNOT_CREATE_DYNAMIC_FILTER = typing___cast(
        FeedItemSetErrorEnum.FeedItemSetErrorValue, 4
    )
    INVALID_FEED_TYPE = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 5)
    DUPLICATE_NAME = typing___cast(FeedItemSetErrorEnum.FeedItemSetErrorValue, 6)
    WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE = typing___cast(
        FeedItemSetErrorEnum.FeedItemSetErrorValue, 7
    )
    type___FeedItemSetError = FeedItemSetError
    def __init__(self,) -> None: ...

type___FeedItemSetErrorEnum = FeedItemSetErrorEnum
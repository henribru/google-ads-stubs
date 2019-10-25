# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class FeedItemTargetErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedItemTargetError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> FeedItemTargetErrorEnum.FeedItemTargetError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[FeedItemTargetErrorEnum.FeedItemTargetError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, FeedItemTargetErrorEnum.FeedItemTargetError]]: ...
        UNSPECIFIED = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 0)
        UNKNOWN = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 1)
        MUST_SET_TARGET_ONEOF_ON_CREATE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 2)
        FEED_ITEM_TARGET_ALREADY_EXISTS = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 3)
        FEED_ITEM_SCHEDULES_CANNOT_OVERLAP = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 4)
        TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 5)
        TOO_MANY_SCHEDULES_PER_DAY = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 6)
        CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 7)
        DUPLICATE_AD_SCHEDULE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 8)
        DUPLICATE_KEYWORD = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 9)
    UNSPECIFIED = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 0)
    UNKNOWN = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 1)
    MUST_SET_TARGET_ONEOF_ON_CREATE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 2)
    FEED_ITEM_TARGET_ALREADY_EXISTS = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 3)
    FEED_ITEM_SCHEDULES_CANNOT_OVERLAP = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 4)
    TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 5)
    TOO_MANY_SCHEDULES_PER_DAY = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 6)
    CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 7)
    DUPLICATE_AD_SCHEDULE = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 8)
    DUPLICATE_KEYWORD = typing___cast(FeedItemTargetErrorEnum.FeedItemTargetError, 9)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FeedItemTargetErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

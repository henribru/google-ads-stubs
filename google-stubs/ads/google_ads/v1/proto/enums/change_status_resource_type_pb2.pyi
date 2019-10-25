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


class ChangeStatusResourceTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ChangeStatusResourceType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> ChangeStatusResourceTypeEnum.ChangeStatusResourceType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[ChangeStatusResourceTypeEnum.ChangeStatusResourceType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, ChangeStatusResourceTypeEnum.ChangeStatusResourceType]]: ...
        UNSPECIFIED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 0)
        UNKNOWN = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 1)
        AD_GROUP = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 3)
        AD_GROUP_AD = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 4)
        AD_GROUP_CRITERION = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 5)
        CAMPAIGN = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 6)
        CAMPAIGN_CRITERION = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 7)
        FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 9)
        FEED_ITEM = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 10)
        AD_GROUP_FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 11)
        CAMPAIGN_FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 12)
        AD_GROUP_BID_MODIFIER = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 13)
    UNSPECIFIED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 0)
    UNKNOWN = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 1)
    AD_GROUP = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 3)
    AD_GROUP_AD = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 4)
    AD_GROUP_CRITERION = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 5)
    CAMPAIGN = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 6)
    CAMPAIGN_CRITERION = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 7)
    FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 9)
    FEED_ITEM = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 10)
    AD_GROUP_FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 11)
    CAMPAIGN_FEED = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 12)
    AD_GROUP_BID_MODIFIER = typing___cast(ChangeStatusResourceTypeEnum.ChangeStatusResourceType, 13)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ChangeStatusResourceTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

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


class BiddingSourceEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BiddingSource(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BiddingSourceEnum.BiddingSource: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BiddingSourceEnum.BiddingSource]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BiddingSourceEnum.BiddingSource]]: ...
        UNSPECIFIED = typing___cast(BiddingSourceEnum.BiddingSource, 0)
        UNKNOWN = typing___cast(BiddingSourceEnum.BiddingSource, 1)
        CAMPAIGN_BIDDING_STRATEGY = typing___cast(BiddingSourceEnum.BiddingSource, 5)
        AD_GROUP = typing___cast(BiddingSourceEnum.BiddingSource, 6)
        AD_GROUP_CRITERION = typing___cast(BiddingSourceEnum.BiddingSource, 7)
    UNSPECIFIED = typing___cast(BiddingSourceEnum.BiddingSource, 0)
    UNKNOWN = typing___cast(BiddingSourceEnum.BiddingSource, 1)
    CAMPAIGN_BIDDING_STRATEGY = typing___cast(BiddingSourceEnum.BiddingSource, 5)
    AD_GROUP = typing___cast(BiddingSourceEnum.BiddingSource, 6)
    AD_GROUP_CRITERION = typing___cast(BiddingSourceEnum.BiddingSource, 7)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BiddingSourceEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

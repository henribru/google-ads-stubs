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


class BiddingStrategyErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BiddingStrategyError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BiddingStrategyErrorEnum.BiddingStrategyError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BiddingStrategyErrorEnum.BiddingStrategyError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BiddingStrategyErrorEnum.BiddingStrategyError]]: ...
        UNSPECIFIED = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 0)
        UNKNOWN = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 1)
        DUPLICATE_NAME = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 2)
        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 3)
        CANNOT_REMOVE_ASSOCIATED_STRATEGY = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 4)
        BIDDING_STRATEGY_NOT_SUPPORTED = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 5)
        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 6)
    UNSPECIFIED = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 0)
    UNKNOWN = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 1)
    DUPLICATE_NAME = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 2)
    CANNOT_CHANGE_BIDDING_STRATEGY_TYPE = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 3)
    CANNOT_REMOVE_ASSOCIATED_STRATEGY = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 4)
    BIDDING_STRATEGY_NOT_SUPPORTED = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 5)
    INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE = typing___cast(BiddingStrategyErrorEnum.BiddingStrategyError, 6)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BiddingStrategyErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

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


class KeywordPlanNetworkEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class KeywordPlanNetwork(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> KeywordPlanNetworkEnum.KeywordPlanNetwork: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[KeywordPlanNetworkEnum.KeywordPlanNetwork]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, KeywordPlanNetworkEnum.KeywordPlanNetwork]]: ...
        UNSPECIFIED = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 0)
        UNKNOWN = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 1)
        GOOGLE_SEARCH = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 2)
        GOOGLE_SEARCH_AND_PARTNERS = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 3)
    UNSPECIFIED = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 0)
    UNKNOWN = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 1)
    GOOGLE_SEARCH = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 2)
    GOOGLE_SEARCH_AND_PARTNERS = typing___cast(KeywordPlanNetworkEnum.KeywordPlanNetwork, 3)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordPlanNetworkEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

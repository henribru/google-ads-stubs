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


class KeywordPlanNegativeKeywordErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class KeywordPlanNegativeKeywordError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError]]: ...
        UNSPECIFIED = typing___cast(KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError, 0)
        UNKNOWN = typing___cast(KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError, 1)
    UNSPECIFIED = typing___cast(KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError, 0)
    UNKNOWN = typing___cast(KeywordPlanNegativeKeywordErrorEnum.KeywordPlanNegativeKeywordError, 1)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordPlanNegativeKeywordErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

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


class AdParameterErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AdParameterError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> AdParameterErrorEnum.AdParameterError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[AdParameterErrorEnum.AdParameterError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, AdParameterErrorEnum.AdParameterError]]: ...
        UNSPECIFIED = typing___cast(AdParameterErrorEnum.AdParameterError, 0)
        UNKNOWN = typing___cast(AdParameterErrorEnum.AdParameterError, 1)
        AD_GROUP_CRITERION_MUST_BE_KEYWORD = typing___cast(AdParameterErrorEnum.AdParameterError, 2)
        INVALID_INSERTION_TEXT_FORMAT = typing___cast(AdParameterErrorEnum.AdParameterError, 3)
    UNSPECIFIED = typing___cast(AdParameterErrorEnum.AdParameterError, 0)
    UNKNOWN = typing___cast(AdParameterErrorEnum.AdParameterError, 1)
    AD_GROUP_CRITERION_MUST_BE_KEYWORD = typing___cast(AdParameterErrorEnum.AdParameterError, 2)
    INVALID_INSERTION_TEXT_FORMAT = typing___cast(AdParameterErrorEnum.AdParameterError, 3)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdParameterErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

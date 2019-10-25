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


class QuotaErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class QuotaError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> QuotaErrorEnum.QuotaError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[QuotaErrorEnum.QuotaError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, QuotaErrorEnum.QuotaError]]: ...
        UNSPECIFIED = typing___cast(QuotaErrorEnum.QuotaError, 0)
        UNKNOWN = typing___cast(QuotaErrorEnum.QuotaError, 1)
        RESOURCE_EXHAUSTED = typing___cast(QuotaErrorEnum.QuotaError, 2)
        ACCESS_PROHIBITED = typing___cast(QuotaErrorEnum.QuotaError, 3)
        RESOURCE_TEMPORARILY_EXHAUSTED = typing___cast(QuotaErrorEnum.QuotaError, 4)
    UNSPECIFIED = typing___cast(QuotaErrorEnum.QuotaError, 0)
    UNKNOWN = typing___cast(QuotaErrorEnum.QuotaError, 1)
    RESOURCE_EXHAUSTED = typing___cast(QuotaErrorEnum.QuotaError, 2)
    ACCESS_PROHIBITED = typing___cast(QuotaErrorEnum.QuotaError, 3)
    RESOURCE_TEMPORARILY_EXHAUSTED = typing___cast(QuotaErrorEnum.QuotaError, 4)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> QuotaErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

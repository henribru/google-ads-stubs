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


class AdvertisingChannelTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AdvertisingChannelType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> AdvertisingChannelTypeEnum.AdvertisingChannelType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[AdvertisingChannelTypeEnum.AdvertisingChannelType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, AdvertisingChannelTypeEnum.AdvertisingChannelType]]: ...
        UNSPECIFIED = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 0)
        UNKNOWN = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 1)
        SEARCH = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 2)
        DISPLAY = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 3)
        SHOPPING = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 4)
        HOTEL = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 5)
        VIDEO = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 6)
        MULTI_CHANNEL = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 7)
    UNSPECIFIED = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 0)
    UNKNOWN = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 1)
    SEARCH = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 2)
    DISPLAY = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 3)
    SHOPPING = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 4)
    HOTEL = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 5)
    VIDEO = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 6)
    MULTI_CHANNEL = typing___cast(AdvertisingChannelTypeEnum.AdvertisingChannelType, 7)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdvertisingChannelTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

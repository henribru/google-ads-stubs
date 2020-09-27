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

class GoogleAdsFieldDataTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    GoogleAdsFieldDataTypeValue = typing___NewType(
        "GoogleAdsFieldDataTypeValue", builtin___int
    )
    type___GoogleAdsFieldDataTypeValue = GoogleAdsFieldDataTypeValue
    GoogleAdsFieldDataType: _GoogleAdsFieldDataType
    class _GoogleAdsFieldDataType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 0
        )
        UNKNOWN = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 1
        )
        BOOLEAN = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 2
        )
        DATE = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 3)
        DOUBLE = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 4
        )
        ENUM = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 5)
        FLOAT = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 6)
        INT32 = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 7)
        INT64 = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 8)
        MESSAGE = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 9
        )
        RESOURCE_NAME = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 10
        )
        STRING = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 11
        )
        UINT64 = typing___cast(
            GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 12
        )
    UNSPECIFIED = typing___cast(
        GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 0
    )
    UNKNOWN = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 1)
    BOOLEAN = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 2)
    DATE = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 3)
    DOUBLE = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 4)
    ENUM = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 5)
    FLOAT = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 6)
    INT32 = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 7)
    INT64 = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 8)
    MESSAGE = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 9)
    RESOURCE_NAME = typing___cast(
        GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 10
    )
    STRING = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 11)
    UINT64 = typing___cast(GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue, 12)
    type___GoogleAdsFieldDataType = GoogleAdsFieldDataType
    def __init__(self,) -> None: ...

type___GoogleAdsFieldDataTypeEnum = GoogleAdsFieldDataTypeEnum

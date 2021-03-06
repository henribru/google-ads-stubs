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

class ChangeClientTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ChangeClientTypeValue = typing___NewType("ChangeClientTypeValue", builtin___int)
    type___ChangeClientTypeValue = ChangeClientTypeValue
    ChangeClientType: _ChangeClientType
    class _ChangeClientType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ChangeClientTypeEnum.ChangeClientTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 0)
        UNKNOWN = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 1)
        GOOGLE_ADS_WEB_CLIENT = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 2
        )
        GOOGLE_ADS_AUTOMATED_RULE = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 3
        )
        GOOGLE_ADS_SCRIPTS = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 4
        )
        GOOGLE_ADS_BULK_UPLOAD = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 5
        )
        GOOGLE_ADS_API = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 6)
        GOOGLE_ADS_EDITOR = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 7)
        GOOGLE_ADS_MOBILE_APP = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 8
        )
        GOOGLE_ADS_RECOMMENDATIONS = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 9
        )
        SEARCH_ADS_360_SYNC = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 10
        )
        SEARCH_ADS_360_POST = typing___cast(
            ChangeClientTypeEnum.ChangeClientTypeValue, 11
        )
        INTERNAL_TOOL = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 12)
        OTHER = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 13)
    UNSPECIFIED = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 0)
    UNKNOWN = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 1)
    GOOGLE_ADS_WEB_CLIENT = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 2)
    GOOGLE_ADS_AUTOMATED_RULE = typing___cast(
        ChangeClientTypeEnum.ChangeClientTypeValue, 3
    )
    GOOGLE_ADS_SCRIPTS = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 4)
    GOOGLE_ADS_BULK_UPLOAD = typing___cast(
        ChangeClientTypeEnum.ChangeClientTypeValue, 5
    )
    GOOGLE_ADS_API = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 6)
    GOOGLE_ADS_EDITOR = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 7)
    GOOGLE_ADS_MOBILE_APP = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 8)
    GOOGLE_ADS_RECOMMENDATIONS = typing___cast(
        ChangeClientTypeEnum.ChangeClientTypeValue, 9
    )
    SEARCH_ADS_360_SYNC = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 10)
    SEARCH_ADS_360_POST = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 11)
    INTERNAL_TOOL = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 12)
    OTHER = typing___cast(ChangeClientTypeEnum.ChangeClientTypeValue, 13)
    type___ChangeClientType = ChangeClientType
    def __init__(self,) -> None: ...

type___ChangeClientTypeEnum = ChangeClientTypeEnum

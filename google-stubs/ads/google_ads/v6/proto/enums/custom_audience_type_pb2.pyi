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

class CustomAudienceTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomAudienceTypeValue = typing___NewType("CustomAudienceTypeValue", builtin___int)
    type___CustomAudienceTypeValue = CustomAudienceTypeValue
    CustomAudienceType: _CustomAudienceType
    class _CustomAudienceType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomAudienceTypeEnum.CustomAudienceTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 0)
        UNKNOWN = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 1)
        AUTO = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 2)
        INTEREST = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 3)
        PURCHASE_INTENT = typing___cast(
            CustomAudienceTypeEnum.CustomAudienceTypeValue, 4
        )
        SEARCH = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 5)
    UNSPECIFIED = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 0)
    UNKNOWN = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 1)
    AUTO = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 2)
    INTEREST = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 3)
    PURCHASE_INTENT = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 4)
    SEARCH = typing___cast(CustomAudienceTypeEnum.CustomAudienceTypeValue, 5)
    type___CustomAudienceType = CustomAudienceType
    def __init__(self,) -> None: ...

type___CustomAudienceTypeEnum = CustomAudienceTypeEnum

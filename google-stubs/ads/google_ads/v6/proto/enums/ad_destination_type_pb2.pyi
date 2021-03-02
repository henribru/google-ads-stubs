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

class AdDestinationTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AdDestinationTypeValue = typing___NewType("AdDestinationTypeValue", builtin___int)
    type___AdDestinationTypeValue = AdDestinationTypeValue
    AdDestinationType: _AdDestinationType
    class _AdDestinationType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AdDestinationTypeEnum.AdDestinationTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 0)
        UNKNOWN = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 1)
        NOT_APPLICABLE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 2)
        WEBSITE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 3)
        APP_DEEP_LINK = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 4)
        APP_STORE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 5)
        PHONE_CALL = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 6)
        MAP_DIRECTIONS = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 7)
        LOCATION_LISTING = typing___cast(
            AdDestinationTypeEnum.AdDestinationTypeValue, 8
        )
        MESSAGE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 9)
        LEAD_FORM = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 10)
        YOUTUBE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 11)
        UNMODELED_FOR_CONVERSIONS = typing___cast(
            AdDestinationTypeEnum.AdDestinationTypeValue, 12
        )
    UNSPECIFIED = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 0)
    UNKNOWN = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 1)
    NOT_APPLICABLE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 2)
    WEBSITE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 3)
    APP_DEEP_LINK = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 4)
    APP_STORE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 5)
    PHONE_CALL = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 6)
    MAP_DIRECTIONS = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 7)
    LOCATION_LISTING = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 8)
    MESSAGE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 9)
    LEAD_FORM = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 10)
    YOUTUBE = typing___cast(AdDestinationTypeEnum.AdDestinationTypeValue, 11)
    UNMODELED_FOR_CONVERSIONS = typing___cast(
        AdDestinationTypeEnum.AdDestinationTypeValue, 12
    )
    type___AdDestinationType = AdDestinationType
    def __init__(self,) -> None: ...

type___AdDestinationTypeEnum = AdDestinationTypeEnum
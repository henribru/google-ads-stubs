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

class LocationExtensionTargetingCriterionFieldEnum(
    google___protobuf___message___Message
):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    LocationExtensionTargetingCriterionFieldValue = typing___NewType(
        "LocationExtensionTargetingCriterionFieldValue", builtin___int
    )
    type___LocationExtensionTargetingCriterionFieldValue = (
        LocationExtensionTargetingCriterionFieldValue
    )
    LocationExtensionTargetingCriterionField: _LocationExtensionTargetingCriterionField
    class _LocationExtensionTargetingCriterionField(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            0,
        )
        UNKNOWN = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            1,
        )
        ADDRESS_LINE_1 = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            2,
        )
        ADDRESS_LINE_2 = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            3,
        )
        CITY = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            4,
        )
        PROVINCE = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            5,
        )
        POSTAL_CODE = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            6,
        )
        COUNTRY_CODE = typing___cast(
            LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
            7,
        )
    UNSPECIFIED = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        0,
    )
    UNKNOWN = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        1,
    )
    ADDRESS_LINE_1 = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        2,
    )
    ADDRESS_LINE_2 = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        3,
    )
    CITY = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        4,
    )
    PROVINCE = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        5,
    )
    POSTAL_CODE = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        6,
    )
    COUNTRY_CODE = typing___cast(
        LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionFieldValue,
        7,
    )
    type___LocationExtensionTargetingCriterionField = (
        LocationExtensionTargetingCriterionField
    )
    def __init__(self,) -> None: ...

type___LocationExtensionTargetingCriterionFieldEnum = (
    LocationExtensionTargetingCriterionFieldEnum
)

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

class CriterionCategoryLocaleAvailabilityModeEnum(
    google___protobuf___message___Message
):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CriterionCategoryLocaleAvailabilityModeValue = typing___NewType(
        "CriterionCategoryLocaleAvailabilityModeValue", builtin___int
    )
    type___CriterionCategoryLocaleAvailabilityModeValue = (
        CriterionCategoryLocaleAvailabilityModeValue
    )
    CriterionCategoryLocaleAvailabilityMode: _CriterionCategoryLocaleAvailabilityMode
    class _CriterionCategoryLocaleAvailabilityMode(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            0,
        )
        UNKNOWN = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            1,
        )
        ALL_LOCALES = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            2,
        )
        COUNTRY_AND_ALL_LANGUAGES = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            3,
        )
        LANGUAGE_AND_ALL_COUNTRIES = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            4,
        )
        COUNTRY_AND_LANGUAGE = typing___cast(
            CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
            5,
        )
    UNSPECIFIED = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        0,
    )
    UNKNOWN = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        1,
    )
    ALL_LOCALES = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        2,
    )
    COUNTRY_AND_ALL_LANGUAGES = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        3,
    )
    LANGUAGE_AND_ALL_COUNTRIES = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        4,
    )
    COUNTRY_AND_LANGUAGE = typing___cast(
        CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityModeValue,
        5,
    )
    type___CriterionCategoryLocaleAvailabilityMode = (
        CriterionCategoryLocaleAvailabilityMode
    )
    def __init__(self,) -> None: ...

type___CriterionCategoryLocaleAvailabilityModeEnum = (
    CriterionCategoryLocaleAvailabilityModeEnum
)
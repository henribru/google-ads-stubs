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

class CustomInterestErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomInterestErrorValue = typing___NewType(
        "CustomInterestErrorValue", builtin___int
    )
    type___CustomInterestErrorValue = CustomInterestErrorValue
    CustomInterestError: _CustomInterestError
    class _CustomInterestError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomInterestErrorEnum.CustomInterestErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CustomInterestErrorEnum.CustomInterestErrorValue, 0)
        UNKNOWN = typing___cast(CustomInterestErrorEnum.CustomInterestErrorValue, 1)
        NAME_ALREADY_USED = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 2
        )
        CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 3
        )
        TYPE_AND_PARAMETER_NOT_FOUND = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 4
        )
        TYPE_AND_PARAMETER_ALREADY_EXISTED = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 5
        )
        INVALID_CUSTOM_INTEREST_MEMBER_TYPE = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 6
        )
        CANNOT_REMOVE_WHILE_IN_USE = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 7
        )
        CANNOT_CHANGE_TYPE = typing___cast(
            CustomInterestErrorEnum.CustomInterestErrorValue, 8
        )
    UNSPECIFIED = typing___cast(CustomInterestErrorEnum.CustomInterestErrorValue, 0)
    UNKNOWN = typing___cast(CustomInterestErrorEnum.CustomInterestErrorValue, 1)
    NAME_ALREADY_USED = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 2
    )
    CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 3
    )
    TYPE_AND_PARAMETER_NOT_FOUND = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 4
    )
    TYPE_AND_PARAMETER_ALREADY_EXISTED = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 5
    )
    INVALID_CUSTOM_INTEREST_MEMBER_TYPE = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 6
    )
    CANNOT_REMOVE_WHILE_IN_USE = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 7
    )
    CANNOT_CHANGE_TYPE = typing___cast(
        CustomInterestErrorEnum.CustomInterestErrorValue, 8
    )
    type___CustomInterestError = CustomInterestError
    def __init__(self,) -> None: ...

type___CustomInterestErrorEnum = CustomInterestErrorEnum

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

class DisplayAdFormatSettingEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DisplayAdFormatSettingValue = typing___NewType(
        "DisplayAdFormatSettingValue", builtin___int
    )
    type___DisplayAdFormatSettingValue = DisplayAdFormatSettingValue
    DisplayAdFormatSetting: _DisplayAdFormatSetting
    class _DisplayAdFormatSetting(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 0
        )
        UNKNOWN = typing___cast(
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 1
        )
        ALL_FORMATS = typing___cast(
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 2
        )
        NON_NATIVE = typing___cast(
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 3
        )
        NATIVE = typing___cast(
            DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 4
        )
    UNSPECIFIED = typing___cast(
        DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 0
    )
    UNKNOWN = typing___cast(DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 1)
    ALL_FORMATS = typing___cast(
        DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 2
    )
    NON_NATIVE = typing___cast(
        DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 3
    )
    NATIVE = typing___cast(DisplayAdFormatSettingEnum.DisplayAdFormatSettingValue, 4)
    type___DisplayAdFormatSetting = DisplayAdFormatSetting
    def __init__(self,) -> None: ...

type___DisplayAdFormatSettingEnum = DisplayAdFormatSettingEnum

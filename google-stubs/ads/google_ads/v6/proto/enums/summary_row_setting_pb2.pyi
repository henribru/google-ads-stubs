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

class SummaryRowSettingEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SummaryRowSettingValue = typing___NewType("SummaryRowSettingValue", builtin___int)
    type___SummaryRowSettingValue = SummaryRowSettingValue
    SummaryRowSetting: _SummaryRowSetting
    class _SummaryRowSetting(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SummaryRowSettingEnum.SummaryRowSettingValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 0)
        UNKNOWN = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 1)
        NO_SUMMARY_ROW = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 2)
        SUMMARY_ROW_WITH_RESULTS = typing___cast(
            SummaryRowSettingEnum.SummaryRowSettingValue, 3
        )
        SUMMARY_ROW_ONLY = typing___cast(
            SummaryRowSettingEnum.SummaryRowSettingValue, 4
        )
    UNSPECIFIED = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 0)
    UNKNOWN = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 1)
    NO_SUMMARY_ROW = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 2)
    SUMMARY_ROW_WITH_RESULTS = typing___cast(
        SummaryRowSettingEnum.SummaryRowSettingValue, 3
    )
    SUMMARY_ROW_ONLY = typing___cast(SummaryRowSettingEnum.SummaryRowSettingValue, 4)
    type___SummaryRowSetting = SummaryRowSetting
    def __init__(self,) -> None: ...

type___SummaryRowSettingEnum = SummaryRowSettingEnum

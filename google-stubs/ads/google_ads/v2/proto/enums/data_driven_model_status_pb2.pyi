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

class DataDrivenModelStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DataDrivenModelStatusValue = typing___NewType(
        "DataDrivenModelStatusValue", builtin___int
    )
    type___DataDrivenModelStatusValue = DataDrivenModelStatusValue
    DataDrivenModelStatus: _DataDrivenModelStatus
    class _DataDrivenModelStatus(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            DataDrivenModelStatusEnum.DataDrivenModelStatusValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 0
        )
        UNKNOWN = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 1)
        AVAILABLE = typing___cast(
            DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 2
        )
        STALE = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 3)
        EXPIRED = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 4)
        NEVER_GENERATED = typing___cast(
            DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 5
        )
    UNSPECIFIED = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 0)
    UNKNOWN = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 1)
    AVAILABLE = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 2)
    STALE = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 3)
    EXPIRED = typing___cast(DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 4)
    NEVER_GENERATED = typing___cast(
        DataDrivenModelStatusEnum.DataDrivenModelStatusValue, 5
    )
    type___DataDrivenModelStatus = DataDrivenModelStatus
    def __init__(self,) -> None: ...

type___DataDrivenModelStatusEnum = DataDrivenModelStatusEnum

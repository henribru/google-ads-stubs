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

class TargetImpressionShareLocationEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    TargetImpressionShareLocationValue = typing___NewType(
        "TargetImpressionShareLocationValue", builtin___int
    )
    type___TargetImpressionShareLocationValue = TargetImpressionShareLocationValue
    TargetImpressionShareLocation: _TargetImpressionShareLocation
    class _TargetImpressionShareLocation(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 0
        )
        UNKNOWN = typing___cast(
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 1
        )
        ANYWHERE_ON_PAGE = typing___cast(
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 2
        )
        TOP_OF_PAGE = typing___cast(
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 3
        )
        ABSOLUTE_TOP_OF_PAGE = typing___cast(
            TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 4
        )
    UNSPECIFIED = typing___cast(
        TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 0
    )
    UNKNOWN = typing___cast(
        TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 1
    )
    ANYWHERE_ON_PAGE = typing___cast(
        TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 2
    )
    TOP_OF_PAGE = typing___cast(
        TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 3
    )
    ABSOLUTE_TOP_OF_PAGE = typing___cast(
        TargetImpressionShareLocationEnum.TargetImpressionShareLocationValue, 4
    )
    type___TargetImpressionShareLocation = TargetImpressionShareLocation
    def __init__(self,) -> None: ...

type___TargetImpressionShareLocationEnum = TargetImpressionShareLocationEnum

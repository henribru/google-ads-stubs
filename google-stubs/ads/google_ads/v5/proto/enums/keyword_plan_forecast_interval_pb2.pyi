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

class KeywordPlanForecastIntervalEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    KeywordPlanForecastIntervalValue = typing___NewType(
        "KeywordPlanForecastIntervalValue", builtin___int
    )
    type___KeywordPlanForecastIntervalValue = KeywordPlanForecastIntervalValue
    KeywordPlanForecastInterval: _KeywordPlanForecastInterval
    class _KeywordPlanForecastInterval(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 0
        )
        UNKNOWN = typing___cast(
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 1
        )
        NEXT_WEEK = typing___cast(
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 3
        )
        NEXT_MONTH = typing___cast(
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 4
        )
        NEXT_QUARTER = typing___cast(
            KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 5
        )
    UNSPECIFIED = typing___cast(
        KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 0
    )
    UNKNOWN = typing___cast(
        KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 1
    )
    NEXT_WEEK = typing___cast(
        KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 3
    )
    NEXT_MONTH = typing___cast(
        KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 4
    )
    NEXT_QUARTER = typing___cast(
        KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalValue, 5
    )
    type___KeywordPlanForecastInterval = KeywordPlanForecastInterval
    def __init__(self,) -> None: ...

type___KeywordPlanForecastIntervalEnum = KeywordPlanForecastIntervalEnum
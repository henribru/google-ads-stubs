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

class TargetCpaOptInRecommendationGoalEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    TargetCpaOptInRecommendationGoalValue = typing___NewType(
        "TargetCpaOptInRecommendationGoalValue", builtin___int
    )
    type___TargetCpaOptInRecommendationGoalValue = TargetCpaOptInRecommendationGoalValue
    TargetCpaOptInRecommendationGoal: _TargetCpaOptInRecommendationGoal
    class _TargetCpaOptInRecommendationGoal(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            0,
        )
        UNKNOWN = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            1,
        )
        SAME_COST = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            2,
        )
        SAME_CONVERSIONS = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            3,
        )
        SAME_CPA = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            4,
        )
        CLOSEST_CPA = typing___cast(
            TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue,
            5,
        )
    UNSPECIFIED = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 0
    )
    UNKNOWN = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 1
    )
    SAME_COST = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 2
    )
    SAME_CONVERSIONS = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 3
    )
    SAME_CPA = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 4
    )
    CLOSEST_CPA = typing___cast(
        TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoalValue, 5
    )
    type___TargetCpaOptInRecommendationGoal = TargetCpaOptInRecommendationGoal
    def __init__(self,) -> None: ...

type___TargetCpaOptInRecommendationGoalEnum = TargetCpaOptInRecommendationGoalEnum

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

class RecommendationTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    RecommendationTypeValue = typing___NewType("RecommendationTypeValue", builtin___int)
    type___RecommendationTypeValue = RecommendationTypeValue
    RecommendationType: _RecommendationType
    class _RecommendationType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            RecommendationTypeEnum.RecommendationTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 0)
        UNKNOWN = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 1)
        CAMPAIGN_BUDGET = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 2
        )
        KEYWORD = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 3)
        TEXT_AD = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 4)
        TARGET_CPA_OPT_IN = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 5
        )
        MAXIMIZE_CONVERSIONS_OPT_IN = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 6
        )
        ENHANCED_CPC_OPT_IN = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 7
        )
        SEARCH_PARTNERS_OPT_IN = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 8
        )
        MAXIMIZE_CLICKS_OPT_IN = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 9
        )
        OPTIMIZE_AD_ROTATION = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 10
        )
        CALLOUT_EXTENSION = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 11
        )
        SITELINK_EXTENSION = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 12
        )
        CALL_EXTENSION = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 13
        )
        KEYWORD_MATCH_TYPE = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 14
        )
        MOVE_UNUSED_BUDGET = typing___cast(
            RecommendationTypeEnum.RecommendationTypeValue, 15
        )
    UNSPECIFIED = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 0)
    UNKNOWN = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 1)
    CAMPAIGN_BUDGET = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 2)
    KEYWORD = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 3)
    TEXT_AD = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 4)
    TARGET_CPA_OPT_IN = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 5)
    MAXIMIZE_CONVERSIONS_OPT_IN = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 6
    )
    ENHANCED_CPC_OPT_IN = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 7
    )
    SEARCH_PARTNERS_OPT_IN = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 8
    )
    MAXIMIZE_CLICKS_OPT_IN = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 9
    )
    OPTIMIZE_AD_ROTATION = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 10
    )
    CALLOUT_EXTENSION = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 11
    )
    SITELINK_EXTENSION = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 12
    )
    CALL_EXTENSION = typing___cast(RecommendationTypeEnum.RecommendationTypeValue, 13)
    KEYWORD_MATCH_TYPE = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 14
    )
    MOVE_UNUSED_BUDGET = typing___cast(
        RecommendationTypeEnum.RecommendationTypeValue, 15
    )
    type___RecommendationType = RecommendationType
    def __init__(self,) -> None: ...

type___RecommendationTypeEnum = RecommendationTypeEnum

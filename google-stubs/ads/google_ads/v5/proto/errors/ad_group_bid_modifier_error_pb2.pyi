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

class AdGroupBidModifierErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AdGroupBidModifierErrorValue = typing___NewType(
        "AdGroupBidModifierErrorValue", builtin___int
    )
    type___AdGroupBidModifierErrorValue = AdGroupBidModifierErrorValue
    AdGroupBidModifierError: _AdGroupBidModifierError
    class _AdGroupBidModifierError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 0
        )
        UNKNOWN = typing___cast(
            AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 1
        )
        CRITERION_ID_NOT_SUPPORTED = typing___cast(
            AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 2
        )
        CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER = typing___cast(
            AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 3
        )
    UNSPECIFIED = typing___cast(
        AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 0
    )
    UNKNOWN = typing___cast(AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 1)
    CRITERION_ID_NOT_SUPPORTED = typing___cast(
        AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 2
    )
    CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER = typing___cast(
        AdGroupBidModifierErrorEnum.AdGroupBidModifierErrorValue, 3
    )
    type___AdGroupBidModifierError = AdGroupBidModifierError
    def __init__(self,) -> None: ...

type___AdGroupBidModifierErrorEnum = AdGroupBidModifierErrorEnum

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

class LeadFormPostSubmitCallToActionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    LeadFormPostSubmitCallToActionTypeValue = typing___NewType(
        "LeadFormPostSubmitCallToActionTypeValue", builtin___int
    )
    type___LeadFormPostSubmitCallToActionTypeValue = (
        LeadFormPostSubmitCallToActionTypeValue
    )
    LeadFormPostSubmitCallToActionType: _LeadFormPostSubmitCallToActionType
    class _LeadFormPostSubmitCallToActionType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            0,
        )
        UNKNOWN = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            1,
        )
        VISIT_SITE = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            2,
        )
        DOWNLOAD = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            3,
        )
        LEARN_MORE = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            4,
        )
        SHOP_NOW = typing___cast(
            LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
            5,
        )
    UNSPECIFIED = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        0,
    )
    UNKNOWN = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        1,
    )
    VISIT_SITE = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        2,
    )
    DOWNLOAD = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        3,
    )
    LEARN_MORE = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        4,
    )
    SHOP_NOW = typing___cast(
        LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionTypeValue,
        5,
    )
    type___LeadFormPostSubmitCallToActionType = LeadFormPostSubmitCallToActionType
    def __init__(self,) -> None: ...

type___LeadFormPostSubmitCallToActionTypeEnum = LeadFormPostSubmitCallToActionTypeEnum

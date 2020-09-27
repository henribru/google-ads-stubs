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

class CampaignCriterionErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CampaignCriterionErrorValue = typing___NewType(
        "CampaignCriterionErrorValue", builtin___int
    )
    type___CampaignCriterionErrorValue = CampaignCriterionErrorValue
    CampaignCriterionError: _CampaignCriterionError
    class _CampaignCriterionError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 0
        )
        UNKNOWN = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 1
        )
        CONCRETE_TYPE_REQUIRED = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 2
        )
        INVALID_PLACEMENT_URL = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 3
        )
        CANNOT_EXCLUDE_CRITERIA_TYPE = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 4
        )
        CANNOT_SET_STATUS_FOR_CRITERIA_TYPE = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 5
        )
        CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 6
        )
        CANNOT_TARGET_AND_EXCLUDE = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 7
        )
        TOO_MANY_OPERATIONS = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 8
        )
        OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 9
        )
        SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 10
        )
        CANNOT_ADD_EXISTING_FIELD = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 11
        )
        CANNOT_UPDATE_NEGATIVE_CRITERION = typing___cast(
            CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 12
        )
    UNSPECIFIED = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 0
    )
    UNKNOWN = typing___cast(CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 1)
    CONCRETE_TYPE_REQUIRED = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 2
    )
    INVALID_PLACEMENT_URL = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 3
    )
    CANNOT_EXCLUDE_CRITERIA_TYPE = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 4
    )
    CANNOT_SET_STATUS_FOR_CRITERIA_TYPE = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 5
    )
    CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 6
    )
    CANNOT_TARGET_AND_EXCLUDE = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 7
    )
    TOO_MANY_OPERATIONS = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 8
    )
    OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 9
    )
    SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 10
    )
    CANNOT_ADD_EXISTING_FIELD = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 11
    )
    CANNOT_UPDATE_NEGATIVE_CRITERION = typing___cast(
        CampaignCriterionErrorEnum.CampaignCriterionErrorValue, 12
    )
    type___CampaignCriterionError = CampaignCriterionError
    def __init__(self,) -> None: ...

type___CampaignCriterionErrorEnum = CampaignCriterionErrorEnum

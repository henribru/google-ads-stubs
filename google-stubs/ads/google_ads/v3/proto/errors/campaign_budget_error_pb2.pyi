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

class CampaignBudgetErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CampaignBudgetErrorValue = typing___NewType(
        "CampaignBudgetErrorValue", builtin___int
    )
    type___CampaignBudgetErrorValue = CampaignBudgetErrorValue
    CampaignBudgetError: _CampaignBudgetError
    class _CampaignBudgetError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 0)
        UNKNOWN = typing___cast(CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 1)
        CAMPAIGN_BUDGET_CANNOT_BE_SHARED = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 17
        )
        CAMPAIGN_BUDGET_REMOVED = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 2
        )
        CAMPAIGN_BUDGET_IN_USE = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 3
        )
        CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 4
        )
        CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 6
        )
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 7
        )
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 8
        )
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 9
        )
        CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 10
        )
        DUPLICATE_NAME = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 11
        )
        MONEY_AMOUNT_IN_WRONG_CURRENCY = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 12
        )
        MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 13
        )
        MONEY_AMOUNT_TOO_LARGE = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 14
        )
        NEGATIVE_MONEY_AMOUNT = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 15
        )
        NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 16
        )
        TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY = typing___cast(
            CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 18
        )
    UNSPECIFIED = typing___cast(CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 0)
    UNKNOWN = typing___cast(CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 1)
    CAMPAIGN_BUDGET_CANNOT_BE_SHARED = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 17
    )
    CAMPAIGN_BUDGET_REMOVED = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 2
    )
    CAMPAIGN_BUDGET_IN_USE = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 3
    )
    CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 4
    )
    CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 6
    )
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 7
    )
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 8
    )
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 9
    )
    CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 10
    )
    DUPLICATE_NAME = typing___cast(CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 11)
    MONEY_AMOUNT_IN_WRONG_CURRENCY = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 12
    )
    MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 13
    )
    MONEY_AMOUNT_TOO_LARGE = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 14
    )
    NEGATIVE_MONEY_AMOUNT = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 15
    )
    NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 16
    )
    TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY = typing___cast(
        CampaignBudgetErrorEnum.CampaignBudgetErrorValue, 18
    )
    type___CampaignBudgetError = CampaignBudgetError
    def __init__(self,) -> None: ...

type___CampaignBudgetErrorEnum = CampaignBudgetErrorEnum

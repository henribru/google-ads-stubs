# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class CampaignErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CampaignError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> CampaignErrorEnum.CampaignError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[CampaignErrorEnum.CampaignError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, CampaignErrorEnum.CampaignError]]: ...
        UNSPECIFIED = typing___cast(CampaignErrorEnum.CampaignError, 0)
        UNKNOWN = typing___cast(CampaignErrorEnum.CampaignError, 1)
        CANNOT_TARGET_CONTENT_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 3)
        CANNOT_TARGET_SEARCH_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 4)
        CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH = typing___cast(CampaignErrorEnum.CampaignError, 5)
        CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN = typing___cast(CampaignErrorEnum.CampaignError, 6)
        CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 7)
        CANNOT_TARGET_PARTNER_SEARCH_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 8)
        CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY = typing___cast(CampaignErrorEnum.CampaignError, 9)
        CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS = typing___cast(CampaignErrorEnum.CampaignError, 10)
        CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN = typing___cast(CampaignErrorEnum.CampaignError, 11)
        DUPLICATE_CAMPAIGN_NAME = typing___cast(CampaignErrorEnum.CampaignError, 12)
        INCOMPATIBLE_CAMPAIGN_FIELD = typing___cast(CampaignErrorEnum.CampaignError, 13)
        INVALID_CAMPAIGN_NAME = typing___cast(CampaignErrorEnum.CampaignError, 14)
        INVALID_AD_SERVING_OPTIMIZATION_STATUS = typing___cast(CampaignErrorEnum.CampaignError, 15)
        INVALID_TRACKING_URL = typing___cast(CampaignErrorEnum.CampaignError, 16)
        CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 17)
        MAX_IMPRESSIONS_NOT_IN_RANGE = typing___cast(CampaignErrorEnum.CampaignError, 18)
        TIME_UNIT_NOT_SUPPORTED = typing___cast(CampaignErrorEnum.CampaignError, 19)
        INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED = typing___cast(CampaignErrorEnum.CampaignError, 20)
        BUDGET_CANNOT_BE_SHARED = typing___cast(CampaignErrorEnum.CampaignError, 21)
        CAMPAIGN_CANNOT_USE_SHARED_BUDGET = typing___cast(CampaignErrorEnum.CampaignError, 22)
        CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS = typing___cast(CampaignErrorEnum.CampaignError, 23)
        CAMPAIGN_LABEL_DOES_NOT_EXIST = typing___cast(CampaignErrorEnum.CampaignError, 24)
        CAMPAIGN_LABEL_ALREADY_EXISTS = typing___cast(CampaignErrorEnum.CampaignError, 25)
        MISSING_SHOPPING_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 26)
        INVALID_SHOPPING_SALES_COUNTRY = typing___cast(CampaignErrorEnum.CampaignError, 27)
        MISSING_UNIVERSAL_APP_CAMPAIGN_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 30)
        ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 31)
        INVALID_ADVERTISING_CHANNEL_SUB_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 32)
        AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED = typing___cast(CampaignErrorEnum.CampaignError, 33)
        CANNOT_SET_AD_ROTATION_MODE = typing___cast(CampaignErrorEnum.CampaignError, 34)
        CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED = typing___cast(CampaignErrorEnum.CampaignError, 35)
        CANNOT_SET_DATE_TO_PAST = typing___cast(CampaignErrorEnum.CampaignError, 36)
        MISSING_HOTEL_CUSTOMER_LINK = typing___cast(CampaignErrorEnum.CampaignError, 37)
        INVALID_HOTEL_CUSTOMER_LINK = typing___cast(CampaignErrorEnum.CampaignError, 38)
        MISSING_HOTEL_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 39)
        CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP = typing___cast(CampaignErrorEnum.CampaignError, 40)
        APP_NOT_FOUND = typing___cast(CampaignErrorEnum.CampaignError, 41)
        SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 42)
        MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS = typing___cast(CampaignErrorEnum.CampaignError, 43)
        INSUFFICIENT_APP_INSTALLS_COUNT = typing___cast(CampaignErrorEnum.CampaignError, 44)
    UNSPECIFIED = typing___cast(CampaignErrorEnum.CampaignError, 0)
    UNKNOWN = typing___cast(CampaignErrorEnum.CampaignError, 1)
    CANNOT_TARGET_CONTENT_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 3)
    CANNOT_TARGET_SEARCH_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 4)
    CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH = typing___cast(CampaignErrorEnum.CampaignError, 5)
    CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN = typing___cast(CampaignErrorEnum.CampaignError, 6)
    CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 7)
    CANNOT_TARGET_PARTNER_SEARCH_NETWORK = typing___cast(CampaignErrorEnum.CampaignError, 8)
    CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY = typing___cast(CampaignErrorEnum.CampaignError, 9)
    CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS = typing___cast(CampaignErrorEnum.CampaignError, 10)
    CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN = typing___cast(CampaignErrorEnum.CampaignError, 11)
    DUPLICATE_CAMPAIGN_NAME = typing___cast(CampaignErrorEnum.CampaignError, 12)
    INCOMPATIBLE_CAMPAIGN_FIELD = typing___cast(CampaignErrorEnum.CampaignError, 13)
    INVALID_CAMPAIGN_NAME = typing___cast(CampaignErrorEnum.CampaignError, 14)
    INVALID_AD_SERVING_OPTIMIZATION_STATUS = typing___cast(CampaignErrorEnum.CampaignError, 15)
    INVALID_TRACKING_URL = typing___cast(CampaignErrorEnum.CampaignError, 16)
    CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 17)
    MAX_IMPRESSIONS_NOT_IN_RANGE = typing___cast(CampaignErrorEnum.CampaignError, 18)
    TIME_UNIT_NOT_SUPPORTED = typing___cast(CampaignErrorEnum.CampaignError, 19)
    INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED = typing___cast(CampaignErrorEnum.CampaignError, 20)
    BUDGET_CANNOT_BE_SHARED = typing___cast(CampaignErrorEnum.CampaignError, 21)
    CAMPAIGN_CANNOT_USE_SHARED_BUDGET = typing___cast(CampaignErrorEnum.CampaignError, 22)
    CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS = typing___cast(CampaignErrorEnum.CampaignError, 23)
    CAMPAIGN_LABEL_DOES_NOT_EXIST = typing___cast(CampaignErrorEnum.CampaignError, 24)
    CAMPAIGN_LABEL_ALREADY_EXISTS = typing___cast(CampaignErrorEnum.CampaignError, 25)
    MISSING_SHOPPING_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 26)
    INVALID_SHOPPING_SALES_COUNTRY = typing___cast(CampaignErrorEnum.CampaignError, 27)
    MISSING_UNIVERSAL_APP_CAMPAIGN_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 30)
    ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 31)
    INVALID_ADVERTISING_CHANNEL_SUB_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 32)
    AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED = typing___cast(CampaignErrorEnum.CampaignError, 33)
    CANNOT_SET_AD_ROTATION_MODE = typing___cast(CampaignErrorEnum.CampaignError, 34)
    CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED = typing___cast(CampaignErrorEnum.CampaignError, 35)
    CANNOT_SET_DATE_TO_PAST = typing___cast(CampaignErrorEnum.CampaignError, 36)
    MISSING_HOTEL_CUSTOMER_LINK = typing___cast(CampaignErrorEnum.CampaignError, 37)
    INVALID_HOTEL_CUSTOMER_LINK = typing___cast(CampaignErrorEnum.CampaignError, 38)
    MISSING_HOTEL_SETTING = typing___cast(CampaignErrorEnum.CampaignError, 39)
    CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP = typing___cast(CampaignErrorEnum.CampaignError, 40)
    APP_NOT_FOUND = typing___cast(CampaignErrorEnum.CampaignError, 41)
    SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE = typing___cast(CampaignErrorEnum.CampaignError, 42)
    MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS = typing___cast(CampaignErrorEnum.CampaignError, 43)
    INSUFFICIENT_APP_INSTALLS_COUNT = typing___cast(CampaignErrorEnum.CampaignError, 44)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CampaignErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

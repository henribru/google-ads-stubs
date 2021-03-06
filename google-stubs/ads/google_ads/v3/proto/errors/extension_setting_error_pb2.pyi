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

class ExtensionSettingErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ExtensionSettingErrorValue = typing___NewType(
        "ExtensionSettingErrorValue", builtin___int
    )
    type___ExtensionSettingErrorValue = ExtensionSettingErrorValue
    ExtensionSettingError: _ExtensionSettingError
    class _ExtensionSettingError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 0
        )
        UNKNOWN = typing___cast(ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 1)
        EXTENSIONS_REQUIRED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 2
        )
        FEED_TYPE_EXTENSION_TYPE_MISMATCH = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 3
        )
        INVALID_FEED_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 4
        )
        INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 5
        )
        CANNOT_CHANGE_FEED_ITEM_ON_CREATE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 6
        )
        CANNOT_UPDATE_NEWLY_CREATED_EXTENSION = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 7
        )
        NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 8
        )
        NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 9
        )
        NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 10
        )
        AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 11
        )
        CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 12
        )
        CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 13
        )
        AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 14
        )
        CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 15
        )
        CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 16
        )
        VALUE_OUT_OF_RANGE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 17
        )
        CANNOT_SET_FIELD_WITH_FINAL_URLS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 18
        )
        FINAL_URLS_NOT_SET = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 19
        )
        INVALID_PHONE_NUMBER = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 20
        )
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 21
        )
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 22
        )
        PREMIUM_RATE_NUMBER_NOT_ALLOWED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 23
        )
        DISALLOWED_NUMBER_TYPE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 24
        )
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 25
        )
        VANITY_PHONE_NUMBER_NOT_ALLOWED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 26
        )
        INVALID_COUNTRY_CODE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 27
        )
        INVALID_CALL_CONVERSION_TYPE_ID = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 28
        )
        CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 29
        )
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 30
        )
        INVALID_APP_ID = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 31
        )
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 32
        )
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 33
        )
        REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 34
        )
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 35
        )
        MISSING_FIELD = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 36
        )
        INCONSISTENT_CURRENCY_CODES = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 37
        )
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 38
        )
        PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 39
        )
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 40
        )
        PRICE_EXTENSION_HAS_TOO_MANY_ITEMS = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 41
        )
        UNSUPPORTED_VALUE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 42
        )
        INVALID_DEVICE_PREFERENCE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 43
        )
        INVALID_SCHEDULE_END = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 45
        )
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 47
        )
        OVERLAPPING_SCHEDULES_NOT_ALLOWED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 48
        )
        SCHEDULE_END_NOT_AFTER_START = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 49
        )
        TOO_MANY_SCHEDULES_PER_DAY = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 50
        )
        DUPLICATE_EXTENSION_FEED_ITEM_EDIT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 51
        )
        INVALID_SNIPPETS_HEADER = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 52
        )
        PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 53
        )
        CAMPAIGN_TARGETING_MISMATCH = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 54
        )
        CANNOT_OPERATE_ON_REMOVED_FEED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 55
        )
        EXTENSION_TYPE_REQUIRED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 56
        )
        INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 57
        )
        START_DATE_AFTER_END_DATE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 58
        )
        INVALID_PRICE_FORMAT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 59
        )
        PROMOTION_INVALID_TIME = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 60
        )
        PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 61
        )
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 62
        )
        TOO_MANY_DECIMAL_PLACES_SPECIFIED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 63
        )
        INVALID_LANGUAGE_CODE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 64
        )
        UNSUPPORTED_LANGUAGE = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 65
        )
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 66
        )
        EXTENSION_SETTING_UPDATE_IS_A_NOOP = typing___cast(
            ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 67
        )
    UNSPECIFIED = typing___cast(ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 0)
    UNKNOWN = typing___cast(ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 1)
    EXTENSIONS_REQUIRED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 2
    )
    FEED_TYPE_EXTENSION_TYPE_MISMATCH = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 3
    )
    INVALID_FEED_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 4
    )
    INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 5
    )
    CANNOT_CHANGE_FEED_ITEM_ON_CREATE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 6
    )
    CANNOT_UPDATE_NEWLY_CREATED_EXTENSION = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 7
    )
    NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 8
    )
    NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 9
    )
    NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 10
    )
    AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 11
    )
    CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 12
    )
    CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 13
    )
    AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 14
    )
    CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 15
    )
    CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 16
    )
    VALUE_OUT_OF_RANGE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 17
    )
    CANNOT_SET_FIELD_WITH_FINAL_URLS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 18
    )
    FINAL_URLS_NOT_SET = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 19
    )
    INVALID_PHONE_NUMBER = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 20
    )
    PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 21
    )
    CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 22
    )
    PREMIUM_RATE_NUMBER_NOT_ALLOWED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 23
    )
    DISALLOWED_NUMBER_TYPE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 24
    )
    INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 25
    )
    VANITY_PHONE_NUMBER_NOT_ALLOWED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 26
    )
    INVALID_COUNTRY_CODE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 27
    )
    INVALID_CALL_CONVERSION_TYPE_ID = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 28
    )
    CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 29
    )
    CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 30
    )
    INVALID_APP_ID = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 31
    )
    QUOTES_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 32
    )
    HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 33
    )
    REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 34
    )
    SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 35
    )
    MISSING_FIELD = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 36
    )
    INCONSISTENT_CURRENCY_CODES = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 37
    )
    PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 38
    )
    PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 39
    )
    PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 40
    )
    PRICE_EXTENSION_HAS_TOO_MANY_ITEMS = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 41
    )
    UNSUPPORTED_VALUE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 42
    )
    INVALID_DEVICE_PREFERENCE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 43
    )
    INVALID_SCHEDULE_END = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 45
    )
    DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 47
    )
    OVERLAPPING_SCHEDULES_NOT_ALLOWED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 48
    )
    SCHEDULE_END_NOT_AFTER_START = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 49
    )
    TOO_MANY_SCHEDULES_PER_DAY = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 50
    )
    DUPLICATE_EXTENSION_FEED_ITEM_EDIT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 51
    )
    INVALID_SNIPPETS_HEADER = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 52
    )
    PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 53
    )
    CAMPAIGN_TARGETING_MISMATCH = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 54
    )
    CANNOT_OPERATE_ON_REMOVED_FEED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 55
    )
    EXTENSION_TYPE_REQUIRED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 56
    )
    INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 57
    )
    START_DATE_AFTER_END_DATE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 58
    )
    INVALID_PRICE_FORMAT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 59
    )
    PROMOTION_INVALID_TIME = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 60
    )
    PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 61
    )
    PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 62
    )
    TOO_MANY_DECIMAL_PLACES_SPECIFIED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 63
    )
    INVALID_LANGUAGE_CODE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 64
    )
    UNSUPPORTED_LANGUAGE = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 65
    )
    CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 66
    )
    EXTENSION_SETTING_UPDATE_IS_A_NOOP = typing___cast(
        ExtensionSettingErrorEnum.ExtensionSettingErrorValue, 67
    )
    type___ExtensionSettingError = ExtensionSettingError
    def __init__(self,) -> None: ...

type___ExtensionSettingErrorEnum = ExtensionSettingErrorEnum

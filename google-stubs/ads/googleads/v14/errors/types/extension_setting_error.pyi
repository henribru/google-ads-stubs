from typing import Any

import proto

class ExtensionSettingErrorEnum(proto.Message):
    class ExtensionSettingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXTENSIONS_REQUIRED = 2
        FEED_TYPE_EXTENSION_TYPE_MISMATCH = 3
        INVALID_FEED_TYPE = 4
        INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING = 5
        CANNOT_CHANGE_FEED_ITEM_ON_CREATE = 6
        CANNOT_UPDATE_NEWLY_CREATED_EXTENSION = 7
        NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE = 8
        NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE = 9
        NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE = 10
        AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS = 11
        CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS = 12
        CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS = 13
        AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 14
        CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 15
        CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 16
        VALUE_OUT_OF_RANGE = 17
        CANNOT_SET_FIELD_WITH_FINAL_URLS = 18
        FINAL_URLS_NOT_SET = 19
        INVALID_PHONE_NUMBER = 20
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = 21
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = 22
        PREMIUM_RATE_NUMBER_NOT_ALLOWED = 23
        DISALLOWED_NUMBER_TYPE = 24
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = 25
        VANITY_PHONE_NUMBER_NOT_ALLOWED = 26
        INVALID_COUNTRY_CODE = 27
        INVALID_CALL_CONVERSION_TYPE_ID = 28
        CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING = 69
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = 30
        INVALID_APP_ID = 31
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET = 32
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = 33
        REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE = 34
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = 35
        MISSING_FIELD = 36
        INCONSISTENT_CURRENCY_CODES = 37
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = 38
        PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = 39
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = 40
        PRICE_EXTENSION_HAS_TOO_MANY_ITEMS = 41
        UNSUPPORTED_VALUE = 42
        INVALID_DEVICE_PREFERENCE = 43
        INVALID_SCHEDULE_END = 45
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE = 47
        OVERLAPPING_SCHEDULES_NOT_ALLOWED = 48
        SCHEDULE_END_NOT_AFTER_START = 49
        TOO_MANY_SCHEDULES_PER_DAY = 50
        DUPLICATE_EXTENSION_FEED_ITEM_EDIT = 51
        INVALID_SNIPPETS_HEADER = 52
        PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY = 53
        CAMPAIGN_TARGETING_MISMATCH = 54
        CANNOT_OPERATE_ON_REMOVED_FEED = 55
        EXTENSION_TYPE_REQUIRED = 56
        INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION = 57
        START_DATE_AFTER_END_DATE = 58
        INVALID_PRICE_FORMAT = 59
        PROMOTION_INVALID_TIME = 60
        PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT = 61
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = 62
        TOO_MANY_DECIMAL_PLACES_SPECIFIED = 63
        INVALID_LANGUAGE_CODE = 64
        UNSUPPORTED_LANGUAGE = 65
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = 66
        EXTENSION_SETTING_UPDATE_IS_A_NOOP = 67
        DISALLOWED_TEXT = 68
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
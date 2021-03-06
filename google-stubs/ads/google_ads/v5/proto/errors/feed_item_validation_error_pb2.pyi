"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeedItemValidationErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FeedItemValidationError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            FeedItemValidationError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = FeedItemValidationErrorEnum.FeedItemValidationError.V(0)
        UNKNOWN = FeedItemValidationErrorEnum.FeedItemValidationError.V(1)
        STRING_TOO_SHORT = FeedItemValidationErrorEnum.FeedItemValidationError.V(2)
        STRING_TOO_LONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(3)
        VALUE_NOT_SPECIFIED = FeedItemValidationErrorEnum.FeedItemValidationError.V(4)
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(5)
        )
        INVALID_PHONE_NUMBER = FeedItemValidationErrorEnum.FeedItemValidationError.V(6)
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(7)
        )
        PREMIUM_RATE_NUMBER_NOT_ALLOWED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(8)
        )
        DISALLOWED_NUMBER_TYPE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            9
        )
        VALUE_OUT_OF_RANGE = FeedItemValidationErrorEnum.FeedItemValidationError.V(10)
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(11)
        )
        CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(99)
        )
        INVALID_COUNTRY_CODE = FeedItemValidationErrorEnum.FeedItemValidationError.V(13)
        INVALID_APP_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(14)
        MISSING_ATTRIBUTES_FOR_FIELDS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(15)
        )
        INVALID_TYPE_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(16)
        INVALID_EMAIL_ADDRESS = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            17
        )
        INVALID_HTTPS_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(18)
        MISSING_DELIVERY_ADDRESS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(19)
        )
        START_DATE_AFTER_END_DATE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(20)
        )
        MISSING_FEED_ITEM_START_TIME = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(21)
        )
        MISSING_FEED_ITEM_END_TIME = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(22)
        )
        MISSING_FEED_ITEM_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(23)
        VANITY_PHONE_NUMBER_NOT_ALLOWED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(24)
        )
        INVALID_REVIEW_EXTENSION_SNIPPET = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(25)
        )
        INVALID_NUMBER_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            26
        )
        INVALID_DATE_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(27)
        INVALID_PRICE_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(28)
        UNKNOWN_PLACEHOLDER_FIELD = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(29)
        )
        MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(30)
        )
        REVIEW_EXTENSION_SOURCE_INELIGIBLE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(31)
        )
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(32)
        )
        DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(33)
        )
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(34)
        )
        INVALID_FORM_ENCODED_PARAMS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(35)
        )
        INVALID_URL_PARAMETER_NAME = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(36)
        )
        NO_GEOCODING_RESULT = FeedItemValidationErrorEnum.FeedItemValidationError.V(37)
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(38)
        )
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(39)
        )
        INVALID_PLACEHOLDER_FIELD_ID = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(40)
        )
        INVALID_URL_TAG = FeedItemValidationErrorEnum.FeedItemValidationError.V(41)
        LIST_TOO_LONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(42)
        INVALID_ATTRIBUTES_COMBINATION = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(43)
        )
        DUPLICATE_VALUES = FeedItemValidationErrorEnum.FeedItemValidationError.V(44)
        INVALID_CALL_CONVERSION_ACTION_ID = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(45)
        )
        CANNOT_SET_WITHOUT_FINAL_URLS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(46)
        )
        APP_ID_DOESNT_EXIST_IN_APP_STORE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(47)
        )
        INVALID_FINAL_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(48)
        INVALID_TRACKING_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(49)
        INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(50)
        )
        LIST_TOO_SHORT = FeedItemValidationErrorEnum.FeedItemValidationError.V(51)
        INVALID_USER_ACTION = FeedItemValidationErrorEnum.FeedItemValidationError.V(52)
        INVALID_TYPE_NAME = FeedItemValidationErrorEnum.FeedItemValidationError.V(53)
        INVALID_EVENT_CHANGE_STATUS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(54)
        )
        INVALID_SNIPPETS_HEADER = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            55
        )
        INVALID_ANDROID_APP_LINK = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(56)
        )
        NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(57)
        )
        RESERVED_KEYWORD_OTHER = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            58
        )
        DUPLICATE_OPTION_LABELS = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            59
        )
        DUPLICATE_OPTION_PREFILLS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(60)
        )
        UNEQUAL_LIST_LENGTHS = FeedItemValidationErrorEnum.FeedItemValidationError.V(61)
        INCONSISTENT_CURRENCY_CODES = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(62)
        )
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(63)
        )
        ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(64)
        )
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(65)
        )
        UNSUPPORTED_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(66)
        INVALID_FINAL_MOBILE_URL = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(67)
        )
        INVALID_KEYWORDLESS_AD_RULE_LABEL = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(68)
        )
        VALUE_TRACK_PARAMETER_NOT_SUPPORTED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(69)
        )
        UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(70)
        )
        INVALID_IOS_APP_LINK = FeedItemValidationErrorEnum.FeedItemValidationError.V(71)
        MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(72)
        )
        PROMOTION_INVALID_TIME = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            73
        )
        PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(74)
        )
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(75)
        )
        TOO_MANY_DECIMAL_PLACES_SPECIFIED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(76)
        )
        AD_CUSTOMIZERS_NOT_ALLOWED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(77)
        )
        INVALID_LANGUAGE_CODE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            78
        )
        UNSUPPORTED_LANGUAGE = FeedItemValidationErrorEnum.FeedItemValidationError.V(79)
        IF_FUNCTION_NOT_ALLOWED = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            80
        )
        INVALID_FINAL_URL_SUFFIX = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(81)
        )
        INVALID_TAG_IN_FINAL_URL_SUFFIX = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(82)
        )
        INVALID_FINAL_URL_SUFFIX_FORMAT = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(83)
        )
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(84)
        )
        ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(85)
        )
        NO_DELIVERY_OPTION_IS_SET = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(86)
        )
        INVALID_CONVERSION_REPORTING_STATE = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(87)
        )
        IMAGE_SIZE_WRONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(88)
        EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(89)
        )
        AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY = (
            FeedItemValidationErrorEnum.FeedItemValidationError.V(90)
        )
        INVALID_LATITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            91
        )
        INVALID_LONGITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            92
        )
        TOO_MANY_LABELS = FeedItemValidationErrorEnum.FeedItemValidationError.V(93)
        INVALID_IMAGE_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(94)
        MISSING_LATITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            95
        )
        MISSING_LONGITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            96
        )
        ADDRESS_NOT_FOUND = FeedItemValidationErrorEnum.FeedItemValidationError.V(97)
        ADDRESS_NOT_TARGETABLE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
            98
        )
    class FeedItemValidationError(metaclass=_FeedItemValidationError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = FeedItemValidationErrorEnum.FeedItemValidationError.V(0)
    UNKNOWN = FeedItemValidationErrorEnum.FeedItemValidationError.V(1)
    STRING_TOO_SHORT = FeedItemValidationErrorEnum.FeedItemValidationError.V(2)
    STRING_TOO_LONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(3)
    VALUE_NOT_SPECIFIED = FeedItemValidationErrorEnum.FeedItemValidationError.V(4)
    INVALID_DOMESTIC_PHONE_NUMBER_FORMAT = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(5)
    )
    INVALID_PHONE_NUMBER = FeedItemValidationErrorEnum.FeedItemValidationError.V(6)
    PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(7)
    )
    PREMIUM_RATE_NUMBER_NOT_ALLOWED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(8)
    )
    DISALLOWED_NUMBER_TYPE = FeedItemValidationErrorEnum.FeedItemValidationError.V(9)
    VALUE_OUT_OF_RANGE = FeedItemValidationErrorEnum.FeedItemValidationError.V(10)
    CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(11)
    )
    CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(99)
    )
    INVALID_COUNTRY_CODE = FeedItemValidationErrorEnum.FeedItemValidationError.V(13)
    INVALID_APP_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(14)
    MISSING_ATTRIBUTES_FOR_FIELDS = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(15)
    )
    INVALID_TYPE_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(16)
    INVALID_EMAIL_ADDRESS = FeedItemValidationErrorEnum.FeedItemValidationError.V(17)
    INVALID_HTTPS_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(18)
    MISSING_DELIVERY_ADDRESS = FeedItemValidationErrorEnum.FeedItemValidationError.V(19)
    START_DATE_AFTER_END_DATE = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        20
    )
    MISSING_FEED_ITEM_START_TIME = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(21)
    )
    MISSING_FEED_ITEM_END_TIME = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        22
    )
    MISSING_FEED_ITEM_ID = FeedItemValidationErrorEnum.FeedItemValidationError.V(23)
    VANITY_PHONE_NUMBER_NOT_ALLOWED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(24)
    )
    INVALID_REVIEW_EXTENSION_SNIPPET = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(25)
    )
    INVALID_NUMBER_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(26)
    INVALID_DATE_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(27)
    INVALID_PRICE_FORMAT = FeedItemValidationErrorEnum.FeedItemValidationError.V(28)
    UNKNOWN_PLACEHOLDER_FIELD = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        29
    )
    MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(30)
    )
    REVIEW_EXTENSION_SOURCE_INELIGIBLE = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(31)
    )
    HYPHENS_IN_REVIEW_EXTENSION_SNIPPET = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(32)
    )
    DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(33)
    )
    QUOTES_IN_REVIEW_EXTENSION_SNIPPET = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(34)
    )
    INVALID_FORM_ENCODED_PARAMS = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        35
    )
    INVALID_URL_PARAMETER_NAME = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        36
    )
    NO_GEOCODING_RESULT = FeedItemValidationErrorEnum.FeedItemValidationError.V(37)
    SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(38)
    )
    CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(39)
    )
    INVALID_PLACEHOLDER_FIELD_ID = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(40)
    )
    INVALID_URL_TAG = FeedItemValidationErrorEnum.FeedItemValidationError.V(41)
    LIST_TOO_LONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(42)
    INVALID_ATTRIBUTES_COMBINATION = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(43)
    )
    DUPLICATE_VALUES = FeedItemValidationErrorEnum.FeedItemValidationError.V(44)
    INVALID_CALL_CONVERSION_ACTION_ID = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(45)
    )
    CANNOT_SET_WITHOUT_FINAL_URLS = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(46)
    )
    APP_ID_DOESNT_EXIST_IN_APP_STORE = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(47)
    )
    INVALID_FINAL_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(48)
    INVALID_TRACKING_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(49)
    INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(50)
    )
    LIST_TOO_SHORT = FeedItemValidationErrorEnum.FeedItemValidationError.V(51)
    INVALID_USER_ACTION = FeedItemValidationErrorEnum.FeedItemValidationError.V(52)
    INVALID_TYPE_NAME = FeedItemValidationErrorEnum.FeedItemValidationError.V(53)
    INVALID_EVENT_CHANGE_STATUS = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        54
    )
    INVALID_SNIPPETS_HEADER = FeedItemValidationErrorEnum.FeedItemValidationError.V(55)
    INVALID_ANDROID_APP_LINK = FeedItemValidationErrorEnum.FeedItemValidationError.V(56)
    NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(57)
    )
    RESERVED_KEYWORD_OTHER = FeedItemValidationErrorEnum.FeedItemValidationError.V(58)
    DUPLICATE_OPTION_LABELS = FeedItemValidationErrorEnum.FeedItemValidationError.V(59)
    DUPLICATE_OPTION_PREFILLS = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        60
    )
    UNEQUAL_LIST_LENGTHS = FeedItemValidationErrorEnum.FeedItemValidationError.V(61)
    INCONSISTENT_CURRENCY_CODES = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        62
    )
    PRICE_EXTENSION_HAS_DUPLICATED_HEADERS = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(63)
    )
    ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(64)
    )
    PRICE_EXTENSION_HAS_TOO_FEW_ITEMS = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(65)
    )
    UNSUPPORTED_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(66)
    INVALID_FINAL_MOBILE_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(67)
    INVALID_KEYWORDLESS_AD_RULE_LABEL = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(68)
    )
    VALUE_TRACK_PARAMETER_NOT_SUPPORTED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(69)
    )
    UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(70)
    )
    INVALID_IOS_APP_LINK = FeedItemValidationErrorEnum.FeedItemValidationError.V(71)
    MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(72)
    )
    PROMOTION_INVALID_TIME = FeedItemValidationErrorEnum.FeedItemValidationError.V(73)
    PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(74)
    )
    PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(75)
    )
    TOO_MANY_DECIMAL_PLACES_SPECIFIED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(76)
    )
    AD_CUSTOMIZERS_NOT_ALLOWED = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        77
    )
    INVALID_LANGUAGE_CODE = FeedItemValidationErrorEnum.FeedItemValidationError.V(78)
    UNSUPPORTED_LANGUAGE = FeedItemValidationErrorEnum.FeedItemValidationError.V(79)
    IF_FUNCTION_NOT_ALLOWED = FeedItemValidationErrorEnum.FeedItemValidationError.V(80)
    INVALID_FINAL_URL_SUFFIX = FeedItemValidationErrorEnum.FeedItemValidationError.V(81)
    INVALID_TAG_IN_FINAL_URL_SUFFIX = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(82)
    )
    INVALID_FINAL_URL_SUFFIX_FORMAT = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(83)
    )
    CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(84)
    )
    ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(85)
    )
    NO_DELIVERY_OPTION_IS_SET = FeedItemValidationErrorEnum.FeedItemValidationError.V(
        86
    )
    INVALID_CONVERSION_REPORTING_STATE = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(87)
    )
    IMAGE_SIZE_WRONG = FeedItemValidationErrorEnum.FeedItemValidationError.V(88)
    EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(89)
    )
    AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY = (
        FeedItemValidationErrorEnum.FeedItemValidationError.V(90)
    )
    INVALID_LATITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(91)
    INVALID_LONGITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(92)
    TOO_MANY_LABELS = FeedItemValidationErrorEnum.FeedItemValidationError.V(93)
    INVALID_IMAGE_URL = FeedItemValidationErrorEnum.FeedItemValidationError.V(94)
    MISSING_LATITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(95)
    MISSING_LONGITUDE_VALUE = FeedItemValidationErrorEnum.FeedItemValidationError.V(96)
    ADDRESS_NOT_FOUND = FeedItemValidationErrorEnum.FeedItemValidationError.V(97)
    ADDRESS_NOT_TARGETABLE = FeedItemValidationErrorEnum.FeedItemValidationError.V(98)
    def __init__(
        self,
    ) -> None: ...

global___FeedItemValidationErrorEnum = FeedItemValidationErrorEnum

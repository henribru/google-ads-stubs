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

class AdErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AdError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AdErrorEnum.AdError.V(0)
        UNKNOWN = AdErrorEnum.AdError.V(1)
        AD_CUSTOMIZERS_NOT_SUPPORTED_FOR_AD_TYPE = AdErrorEnum.AdError.V(2)
        APPROXIMATELY_TOO_LONG = AdErrorEnum.AdError.V(3)
        APPROXIMATELY_TOO_SHORT = AdErrorEnum.AdError.V(4)
        BAD_SNIPPET = AdErrorEnum.AdError.V(5)
        CANNOT_MODIFY_AD = AdErrorEnum.AdError.V(6)
        CANNOT_SET_BUSINESS_NAME_IF_URL_SET = AdErrorEnum.AdError.V(7)
        CANNOT_SET_FIELD = AdErrorEnum.AdError.V(8)
        CANNOT_SET_FIELD_WITH_ORIGIN_AD_ID_SET = AdErrorEnum.AdError.V(9)
        CANNOT_SET_FIELD_WITH_AD_ID_SET_FOR_SHARING = AdErrorEnum.AdError.V(10)
        CANNOT_SET_ALLOW_FLEXIBLE_COLOR_FALSE = AdErrorEnum.AdError.V(11)
        CANNOT_SET_COLOR_CONTROL_WHEN_NATIVE_FORMAT_SETTING = AdErrorEnum.AdError.V(12)
        CANNOT_SET_URL = AdErrorEnum.AdError.V(13)
        CANNOT_SET_WITHOUT_FINAL_URLS = AdErrorEnum.AdError.V(14)
        CANNOT_SET_WITH_FINAL_URLS = AdErrorEnum.AdError.V(15)
        CANNOT_SET_WITH_URL_DATA = AdErrorEnum.AdError.V(17)
        CANNOT_USE_AD_SUBCLASS_FOR_OPERATOR = AdErrorEnum.AdError.V(18)
        CUSTOMER_NOT_APPROVED_MOBILEADS = AdErrorEnum.AdError.V(19)
        CUSTOMER_NOT_APPROVED_THIRDPARTY_ADS = AdErrorEnum.AdError.V(20)
        CUSTOMER_NOT_APPROVED_THIRDPARTY_REDIRECT_ADS = AdErrorEnum.AdError.V(21)
        CUSTOMER_NOT_ELIGIBLE = AdErrorEnum.AdError.V(22)
        CUSTOMER_NOT_ELIGIBLE_FOR_UPDATING_BEACON_URL = AdErrorEnum.AdError.V(23)
        DIMENSION_ALREADY_IN_UNION = AdErrorEnum.AdError.V(24)
        DIMENSION_MUST_BE_SET = AdErrorEnum.AdError.V(25)
        DIMENSION_NOT_IN_UNION = AdErrorEnum.AdError.V(26)
        DISPLAY_URL_CANNOT_BE_SPECIFIED = AdErrorEnum.AdError.V(27)
        DOMESTIC_PHONE_NUMBER_FORMAT = AdErrorEnum.AdError.V(28)
        EMERGENCY_PHONE_NUMBER = AdErrorEnum.AdError.V(29)
        EMPTY_FIELD = AdErrorEnum.AdError.V(30)
        FEED_ATTRIBUTE_MUST_HAVE_MAPPING_FOR_TYPE_ID = AdErrorEnum.AdError.V(31)
        FEED_ATTRIBUTE_MAPPING_TYPE_MISMATCH = AdErrorEnum.AdError.V(32)
        ILLEGAL_AD_CUSTOMIZER_TAG_USE = AdErrorEnum.AdError.V(33)
        ILLEGAL_TAG_USE = AdErrorEnum.AdError.V(34)
        INCONSISTENT_DIMENSIONS = AdErrorEnum.AdError.V(35)
        INCONSISTENT_STATUS_IN_TEMPLATE_UNION = AdErrorEnum.AdError.V(36)
        INCORRECT_LENGTH = AdErrorEnum.AdError.V(37)
        INELIGIBLE_FOR_UPGRADE = AdErrorEnum.AdError.V(38)
        INVALID_AD_ADDRESS_CAMPAIGN_TARGET = AdErrorEnum.AdError.V(39)
        INVALID_AD_TYPE = AdErrorEnum.AdError.V(40)
        INVALID_ATTRIBUTES_FOR_MOBILE_IMAGE = AdErrorEnum.AdError.V(41)
        INVALID_ATTRIBUTES_FOR_MOBILE_TEXT = AdErrorEnum.AdError.V(42)
        INVALID_CALL_TO_ACTION_TEXT = AdErrorEnum.AdError.V(43)
        INVALID_CHARACTER_FOR_URL = AdErrorEnum.AdError.V(44)
        INVALID_COUNTRY_CODE = AdErrorEnum.AdError.V(45)
        INVALID_EXPANDED_DYNAMIC_SEARCH_AD_TAG = AdErrorEnum.AdError.V(47)
        INVALID_INPUT = AdErrorEnum.AdError.V(48)
        INVALID_MARKUP_LANGUAGE = AdErrorEnum.AdError.V(49)
        INVALID_MOBILE_CARRIER = AdErrorEnum.AdError.V(50)
        INVALID_MOBILE_CARRIER_TARGET = AdErrorEnum.AdError.V(51)
        INVALID_NUMBER_OF_ELEMENTS = AdErrorEnum.AdError.V(52)
        INVALID_PHONE_NUMBER_FORMAT = AdErrorEnum.AdError.V(53)
        INVALID_RICH_MEDIA_CERTIFIED_VENDOR_FORMAT_ID = AdErrorEnum.AdError.V(54)
        INVALID_TEMPLATE_DATA = AdErrorEnum.AdError.V(55)
        INVALID_TEMPLATE_ELEMENT_FIELD_TYPE = AdErrorEnum.AdError.V(56)
        INVALID_TEMPLATE_ID = AdErrorEnum.AdError.V(57)
        LINE_TOO_WIDE = AdErrorEnum.AdError.V(58)
        MISSING_AD_CUSTOMIZER_MAPPING = AdErrorEnum.AdError.V(59)
        MISSING_ADDRESS_COMPONENT = AdErrorEnum.AdError.V(60)
        MISSING_ADVERTISEMENT_NAME = AdErrorEnum.AdError.V(61)
        MISSING_BUSINESS_NAME = AdErrorEnum.AdError.V(62)
        MISSING_DESCRIPTION1 = AdErrorEnum.AdError.V(63)
        MISSING_DESCRIPTION2 = AdErrorEnum.AdError.V(64)
        MISSING_DESTINATION_URL_TAG = AdErrorEnum.AdError.V(65)
        MISSING_LANDING_PAGE_URL_TAG = AdErrorEnum.AdError.V(66)
        MISSING_DIMENSION = AdErrorEnum.AdError.V(67)
        MISSING_DISPLAY_URL = AdErrorEnum.AdError.V(68)
        MISSING_HEADLINE = AdErrorEnum.AdError.V(69)
        MISSING_HEIGHT = AdErrorEnum.AdError.V(70)
        MISSING_IMAGE = AdErrorEnum.AdError.V(71)
        MISSING_MARKETING_IMAGE_OR_PRODUCT_VIDEOS = AdErrorEnum.AdError.V(72)
        MISSING_MARKUP_LANGUAGES = AdErrorEnum.AdError.V(73)
        MISSING_MOBILE_CARRIER = AdErrorEnum.AdError.V(74)
        MISSING_PHONE = AdErrorEnum.AdError.V(75)
        MISSING_REQUIRED_TEMPLATE_FIELDS = AdErrorEnum.AdError.V(76)
        MISSING_TEMPLATE_FIELD_VALUE = AdErrorEnum.AdError.V(77)
        MISSING_TEXT = AdErrorEnum.AdError.V(78)
        MISSING_VISIBLE_URL = AdErrorEnum.AdError.V(79)
        MISSING_WIDTH = AdErrorEnum.AdError.V(80)
        MULTIPLE_DISTINCT_FEEDS_UNSUPPORTED = AdErrorEnum.AdError.V(81)
        MUST_USE_TEMP_AD_UNION_ID_ON_ADD = AdErrorEnum.AdError.V(82)
        TOO_LONG = AdErrorEnum.AdError.V(83)
        TOO_SHORT = AdErrorEnum.AdError.V(84)
        UNION_DIMENSIONS_CANNOT_CHANGE = AdErrorEnum.AdError.V(85)
        UNKNOWN_ADDRESS_COMPONENT = AdErrorEnum.AdError.V(86)
        UNKNOWN_FIELD_NAME = AdErrorEnum.AdError.V(87)
        UNKNOWN_UNIQUE_NAME = AdErrorEnum.AdError.V(88)
        UNSUPPORTED_DIMENSIONS = AdErrorEnum.AdError.V(89)
        URL_INVALID_SCHEME = AdErrorEnum.AdError.V(90)
        URL_INVALID_TOP_LEVEL_DOMAIN = AdErrorEnum.AdError.V(91)
        URL_MALFORMED = AdErrorEnum.AdError.V(92)
        URL_NO_HOST = AdErrorEnum.AdError.V(93)
        URL_NOT_EQUIVALENT = AdErrorEnum.AdError.V(94)
        URL_HOST_NAME_TOO_LONG = AdErrorEnum.AdError.V(95)
        URL_NO_SCHEME = AdErrorEnum.AdError.V(96)
        URL_NO_TOP_LEVEL_DOMAIN = AdErrorEnum.AdError.V(97)
        URL_PATH_NOT_ALLOWED = AdErrorEnum.AdError.V(98)
        URL_PORT_NOT_ALLOWED = AdErrorEnum.AdError.V(99)
        URL_QUERY_NOT_ALLOWED = AdErrorEnum.AdError.V(100)
        URL_SCHEME_BEFORE_EXPANDED_DYNAMIC_SEARCH_AD_TAG = AdErrorEnum.AdError.V(102)
        USER_DOES_NOT_HAVE_ACCESS_TO_TEMPLATE = AdErrorEnum.AdError.V(103)
        INCONSISTENT_EXPANDABLE_SETTINGS = AdErrorEnum.AdError.V(104)
        INVALID_FORMAT = AdErrorEnum.AdError.V(105)
        INVALID_FIELD_TEXT = AdErrorEnum.AdError.V(106)
        ELEMENT_NOT_PRESENT = AdErrorEnum.AdError.V(107)
        IMAGE_ERROR = AdErrorEnum.AdError.V(108)
        VALUE_NOT_IN_RANGE = AdErrorEnum.AdError.V(109)
        FIELD_NOT_PRESENT = AdErrorEnum.AdError.V(110)
        ADDRESS_NOT_COMPLETE = AdErrorEnum.AdError.V(111)
        ADDRESS_INVALID = AdErrorEnum.AdError.V(112)
        VIDEO_RETRIEVAL_ERROR = AdErrorEnum.AdError.V(113)
        AUDIO_ERROR = AdErrorEnum.AdError.V(114)
        INVALID_YOUTUBE_DISPLAY_URL = AdErrorEnum.AdError.V(115)
        TOO_MANY_PRODUCT_IMAGES = AdErrorEnum.AdError.V(116)
        TOO_MANY_PRODUCT_VIDEOS = AdErrorEnum.AdError.V(117)
        INCOMPATIBLE_AD_TYPE_AND_DEVICE_PREFERENCE = AdErrorEnum.AdError.V(118)
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = AdErrorEnum.AdError.V(119)
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(120)
        DISALLOWED_NUMBER_TYPE = AdErrorEnum.AdError.V(121)
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = AdErrorEnum.AdError.V(122)
        PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY = (
            AdErrorEnum.AdError.V(123)
        )
        PREMIUM_RATE_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(124)
        VANITY_PHONE_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(125)
        INVALID_CALL_CONVERSION_TYPE_ID = AdErrorEnum.AdError.V(126)
        CANNOT_DISABLE_CALL_CONVERSION_AND_SET_CONVERSION_TYPE_ID = (
            AdErrorEnum.AdError.V(127)
        )
        CANNOT_SET_PATH2_WITHOUT_PATH1 = AdErrorEnum.AdError.V(128)
        MISSING_DYNAMIC_SEARCH_ADS_SETTING_DOMAIN_NAME = AdErrorEnum.AdError.V(129)
        INCOMPATIBLE_WITH_RESTRICTION_TYPE = AdErrorEnum.AdError.V(130)
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = AdErrorEnum.AdError.V(131)
        MISSING_IMAGE_OR_MEDIA_BUNDLE = AdErrorEnum.AdError.V(132)
        PRODUCT_TYPE_NOT_SUPPORTED_IN_THIS_CAMPAIGN = AdErrorEnum.AdError.V(133)
        PLACEHOLDER_CANNOT_HAVE_EMPTY_DEFAULT_VALUE = AdErrorEnum.AdError.V(134)
        PLACEHOLDER_COUNTDOWN_FUNCTION_CANNOT_HAVE_DEFAULT_VALUE = (
            AdErrorEnum.AdError.V(135)
        )
        PLACEHOLDER_DEFAULT_VALUE_MISSING = AdErrorEnum.AdError.V(136)
        UNEXPECTED_PLACEHOLDER_DEFAULT_VALUE = AdErrorEnum.AdError.V(137)
        AD_CUSTOMIZERS_MAY_NOT_BE_ADJACENT = AdErrorEnum.AdError.V(138)
        UPDATING_AD_WITH_NO_ENABLED_ASSOCIATION = AdErrorEnum.AdError.V(139)
        TOO_MANY_AD_CUSTOMIZERS = AdErrorEnum.AdError.V(141)
        INVALID_AD_CUSTOMIZER_FORMAT = AdErrorEnum.AdError.V(142)
        NESTED_AD_CUSTOMIZER_SYNTAX = AdErrorEnum.AdError.V(143)
        UNSUPPORTED_AD_CUSTOMIZER_SYNTAX = AdErrorEnum.AdError.V(144)
        UNPAIRED_BRACE_IN_AD_CUSTOMIZER_TAG = AdErrorEnum.AdError.V(145)
        MORE_THAN_ONE_COUNTDOWN_TAG_TYPE_EXISTS = AdErrorEnum.AdError.V(146)
        DATE_TIME_IN_COUNTDOWN_TAG_IS_INVALID = AdErrorEnum.AdError.V(147)
        DATE_TIME_IN_COUNTDOWN_TAG_IS_PAST = AdErrorEnum.AdError.V(148)
        UNRECOGNIZED_AD_CUSTOMIZER_TAG_FOUND = AdErrorEnum.AdError.V(149)
    class AdError(metaclass=_AdError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AdErrorEnum.AdError.V(0)
    UNKNOWN = AdErrorEnum.AdError.V(1)
    AD_CUSTOMIZERS_NOT_SUPPORTED_FOR_AD_TYPE = AdErrorEnum.AdError.V(2)
    APPROXIMATELY_TOO_LONG = AdErrorEnum.AdError.V(3)
    APPROXIMATELY_TOO_SHORT = AdErrorEnum.AdError.V(4)
    BAD_SNIPPET = AdErrorEnum.AdError.V(5)
    CANNOT_MODIFY_AD = AdErrorEnum.AdError.V(6)
    CANNOT_SET_BUSINESS_NAME_IF_URL_SET = AdErrorEnum.AdError.V(7)
    CANNOT_SET_FIELD = AdErrorEnum.AdError.V(8)
    CANNOT_SET_FIELD_WITH_ORIGIN_AD_ID_SET = AdErrorEnum.AdError.V(9)
    CANNOT_SET_FIELD_WITH_AD_ID_SET_FOR_SHARING = AdErrorEnum.AdError.V(10)
    CANNOT_SET_ALLOW_FLEXIBLE_COLOR_FALSE = AdErrorEnum.AdError.V(11)
    CANNOT_SET_COLOR_CONTROL_WHEN_NATIVE_FORMAT_SETTING = AdErrorEnum.AdError.V(12)
    CANNOT_SET_URL = AdErrorEnum.AdError.V(13)
    CANNOT_SET_WITHOUT_FINAL_URLS = AdErrorEnum.AdError.V(14)
    CANNOT_SET_WITH_FINAL_URLS = AdErrorEnum.AdError.V(15)
    CANNOT_SET_WITH_URL_DATA = AdErrorEnum.AdError.V(17)
    CANNOT_USE_AD_SUBCLASS_FOR_OPERATOR = AdErrorEnum.AdError.V(18)
    CUSTOMER_NOT_APPROVED_MOBILEADS = AdErrorEnum.AdError.V(19)
    CUSTOMER_NOT_APPROVED_THIRDPARTY_ADS = AdErrorEnum.AdError.V(20)
    CUSTOMER_NOT_APPROVED_THIRDPARTY_REDIRECT_ADS = AdErrorEnum.AdError.V(21)
    CUSTOMER_NOT_ELIGIBLE = AdErrorEnum.AdError.V(22)
    CUSTOMER_NOT_ELIGIBLE_FOR_UPDATING_BEACON_URL = AdErrorEnum.AdError.V(23)
    DIMENSION_ALREADY_IN_UNION = AdErrorEnum.AdError.V(24)
    DIMENSION_MUST_BE_SET = AdErrorEnum.AdError.V(25)
    DIMENSION_NOT_IN_UNION = AdErrorEnum.AdError.V(26)
    DISPLAY_URL_CANNOT_BE_SPECIFIED = AdErrorEnum.AdError.V(27)
    DOMESTIC_PHONE_NUMBER_FORMAT = AdErrorEnum.AdError.V(28)
    EMERGENCY_PHONE_NUMBER = AdErrorEnum.AdError.V(29)
    EMPTY_FIELD = AdErrorEnum.AdError.V(30)
    FEED_ATTRIBUTE_MUST_HAVE_MAPPING_FOR_TYPE_ID = AdErrorEnum.AdError.V(31)
    FEED_ATTRIBUTE_MAPPING_TYPE_MISMATCH = AdErrorEnum.AdError.V(32)
    ILLEGAL_AD_CUSTOMIZER_TAG_USE = AdErrorEnum.AdError.V(33)
    ILLEGAL_TAG_USE = AdErrorEnum.AdError.V(34)
    INCONSISTENT_DIMENSIONS = AdErrorEnum.AdError.V(35)
    INCONSISTENT_STATUS_IN_TEMPLATE_UNION = AdErrorEnum.AdError.V(36)
    INCORRECT_LENGTH = AdErrorEnum.AdError.V(37)
    INELIGIBLE_FOR_UPGRADE = AdErrorEnum.AdError.V(38)
    INVALID_AD_ADDRESS_CAMPAIGN_TARGET = AdErrorEnum.AdError.V(39)
    INVALID_AD_TYPE = AdErrorEnum.AdError.V(40)
    INVALID_ATTRIBUTES_FOR_MOBILE_IMAGE = AdErrorEnum.AdError.V(41)
    INVALID_ATTRIBUTES_FOR_MOBILE_TEXT = AdErrorEnum.AdError.V(42)
    INVALID_CALL_TO_ACTION_TEXT = AdErrorEnum.AdError.V(43)
    INVALID_CHARACTER_FOR_URL = AdErrorEnum.AdError.V(44)
    INVALID_COUNTRY_CODE = AdErrorEnum.AdError.V(45)
    INVALID_EXPANDED_DYNAMIC_SEARCH_AD_TAG = AdErrorEnum.AdError.V(47)
    INVALID_INPUT = AdErrorEnum.AdError.V(48)
    INVALID_MARKUP_LANGUAGE = AdErrorEnum.AdError.V(49)
    INVALID_MOBILE_CARRIER = AdErrorEnum.AdError.V(50)
    INVALID_MOBILE_CARRIER_TARGET = AdErrorEnum.AdError.V(51)
    INVALID_NUMBER_OF_ELEMENTS = AdErrorEnum.AdError.V(52)
    INVALID_PHONE_NUMBER_FORMAT = AdErrorEnum.AdError.V(53)
    INVALID_RICH_MEDIA_CERTIFIED_VENDOR_FORMAT_ID = AdErrorEnum.AdError.V(54)
    INVALID_TEMPLATE_DATA = AdErrorEnum.AdError.V(55)
    INVALID_TEMPLATE_ELEMENT_FIELD_TYPE = AdErrorEnum.AdError.V(56)
    INVALID_TEMPLATE_ID = AdErrorEnum.AdError.V(57)
    LINE_TOO_WIDE = AdErrorEnum.AdError.V(58)
    MISSING_AD_CUSTOMIZER_MAPPING = AdErrorEnum.AdError.V(59)
    MISSING_ADDRESS_COMPONENT = AdErrorEnum.AdError.V(60)
    MISSING_ADVERTISEMENT_NAME = AdErrorEnum.AdError.V(61)
    MISSING_BUSINESS_NAME = AdErrorEnum.AdError.V(62)
    MISSING_DESCRIPTION1 = AdErrorEnum.AdError.V(63)
    MISSING_DESCRIPTION2 = AdErrorEnum.AdError.V(64)
    MISSING_DESTINATION_URL_TAG = AdErrorEnum.AdError.V(65)
    MISSING_LANDING_PAGE_URL_TAG = AdErrorEnum.AdError.V(66)
    MISSING_DIMENSION = AdErrorEnum.AdError.V(67)
    MISSING_DISPLAY_URL = AdErrorEnum.AdError.V(68)
    MISSING_HEADLINE = AdErrorEnum.AdError.V(69)
    MISSING_HEIGHT = AdErrorEnum.AdError.V(70)
    MISSING_IMAGE = AdErrorEnum.AdError.V(71)
    MISSING_MARKETING_IMAGE_OR_PRODUCT_VIDEOS = AdErrorEnum.AdError.V(72)
    MISSING_MARKUP_LANGUAGES = AdErrorEnum.AdError.V(73)
    MISSING_MOBILE_CARRIER = AdErrorEnum.AdError.V(74)
    MISSING_PHONE = AdErrorEnum.AdError.V(75)
    MISSING_REQUIRED_TEMPLATE_FIELDS = AdErrorEnum.AdError.V(76)
    MISSING_TEMPLATE_FIELD_VALUE = AdErrorEnum.AdError.V(77)
    MISSING_TEXT = AdErrorEnum.AdError.V(78)
    MISSING_VISIBLE_URL = AdErrorEnum.AdError.V(79)
    MISSING_WIDTH = AdErrorEnum.AdError.V(80)
    MULTIPLE_DISTINCT_FEEDS_UNSUPPORTED = AdErrorEnum.AdError.V(81)
    MUST_USE_TEMP_AD_UNION_ID_ON_ADD = AdErrorEnum.AdError.V(82)
    TOO_LONG = AdErrorEnum.AdError.V(83)
    TOO_SHORT = AdErrorEnum.AdError.V(84)
    UNION_DIMENSIONS_CANNOT_CHANGE = AdErrorEnum.AdError.V(85)
    UNKNOWN_ADDRESS_COMPONENT = AdErrorEnum.AdError.V(86)
    UNKNOWN_FIELD_NAME = AdErrorEnum.AdError.V(87)
    UNKNOWN_UNIQUE_NAME = AdErrorEnum.AdError.V(88)
    UNSUPPORTED_DIMENSIONS = AdErrorEnum.AdError.V(89)
    URL_INVALID_SCHEME = AdErrorEnum.AdError.V(90)
    URL_INVALID_TOP_LEVEL_DOMAIN = AdErrorEnum.AdError.V(91)
    URL_MALFORMED = AdErrorEnum.AdError.V(92)
    URL_NO_HOST = AdErrorEnum.AdError.V(93)
    URL_NOT_EQUIVALENT = AdErrorEnum.AdError.V(94)
    URL_HOST_NAME_TOO_LONG = AdErrorEnum.AdError.V(95)
    URL_NO_SCHEME = AdErrorEnum.AdError.V(96)
    URL_NO_TOP_LEVEL_DOMAIN = AdErrorEnum.AdError.V(97)
    URL_PATH_NOT_ALLOWED = AdErrorEnum.AdError.V(98)
    URL_PORT_NOT_ALLOWED = AdErrorEnum.AdError.V(99)
    URL_QUERY_NOT_ALLOWED = AdErrorEnum.AdError.V(100)
    URL_SCHEME_BEFORE_EXPANDED_DYNAMIC_SEARCH_AD_TAG = AdErrorEnum.AdError.V(102)
    USER_DOES_NOT_HAVE_ACCESS_TO_TEMPLATE = AdErrorEnum.AdError.V(103)
    INCONSISTENT_EXPANDABLE_SETTINGS = AdErrorEnum.AdError.V(104)
    INVALID_FORMAT = AdErrorEnum.AdError.V(105)
    INVALID_FIELD_TEXT = AdErrorEnum.AdError.V(106)
    ELEMENT_NOT_PRESENT = AdErrorEnum.AdError.V(107)
    IMAGE_ERROR = AdErrorEnum.AdError.V(108)
    VALUE_NOT_IN_RANGE = AdErrorEnum.AdError.V(109)
    FIELD_NOT_PRESENT = AdErrorEnum.AdError.V(110)
    ADDRESS_NOT_COMPLETE = AdErrorEnum.AdError.V(111)
    ADDRESS_INVALID = AdErrorEnum.AdError.V(112)
    VIDEO_RETRIEVAL_ERROR = AdErrorEnum.AdError.V(113)
    AUDIO_ERROR = AdErrorEnum.AdError.V(114)
    INVALID_YOUTUBE_DISPLAY_URL = AdErrorEnum.AdError.V(115)
    TOO_MANY_PRODUCT_IMAGES = AdErrorEnum.AdError.V(116)
    TOO_MANY_PRODUCT_VIDEOS = AdErrorEnum.AdError.V(117)
    INCOMPATIBLE_AD_TYPE_AND_DEVICE_PREFERENCE = AdErrorEnum.AdError.V(118)
    CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY = AdErrorEnum.AdError.V(119)
    CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(120)
    DISALLOWED_NUMBER_TYPE = AdErrorEnum.AdError.V(121)
    PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY = AdErrorEnum.AdError.V(122)
    PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY = AdErrorEnum.AdError.V(
        123
    )
    PREMIUM_RATE_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(124)
    VANITY_PHONE_NUMBER_NOT_ALLOWED = AdErrorEnum.AdError.V(125)
    INVALID_CALL_CONVERSION_TYPE_ID = AdErrorEnum.AdError.V(126)
    CANNOT_DISABLE_CALL_CONVERSION_AND_SET_CONVERSION_TYPE_ID = AdErrorEnum.AdError.V(
        127
    )
    CANNOT_SET_PATH2_WITHOUT_PATH1 = AdErrorEnum.AdError.V(128)
    MISSING_DYNAMIC_SEARCH_ADS_SETTING_DOMAIN_NAME = AdErrorEnum.AdError.V(129)
    INCOMPATIBLE_WITH_RESTRICTION_TYPE = AdErrorEnum.AdError.V(130)
    CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED = AdErrorEnum.AdError.V(131)
    MISSING_IMAGE_OR_MEDIA_BUNDLE = AdErrorEnum.AdError.V(132)
    PRODUCT_TYPE_NOT_SUPPORTED_IN_THIS_CAMPAIGN = AdErrorEnum.AdError.V(133)
    PLACEHOLDER_CANNOT_HAVE_EMPTY_DEFAULT_VALUE = AdErrorEnum.AdError.V(134)
    PLACEHOLDER_COUNTDOWN_FUNCTION_CANNOT_HAVE_DEFAULT_VALUE = AdErrorEnum.AdError.V(
        135
    )
    PLACEHOLDER_DEFAULT_VALUE_MISSING = AdErrorEnum.AdError.V(136)
    UNEXPECTED_PLACEHOLDER_DEFAULT_VALUE = AdErrorEnum.AdError.V(137)
    AD_CUSTOMIZERS_MAY_NOT_BE_ADJACENT = AdErrorEnum.AdError.V(138)
    UPDATING_AD_WITH_NO_ENABLED_ASSOCIATION = AdErrorEnum.AdError.V(139)
    TOO_MANY_AD_CUSTOMIZERS = AdErrorEnum.AdError.V(141)
    INVALID_AD_CUSTOMIZER_FORMAT = AdErrorEnum.AdError.V(142)
    NESTED_AD_CUSTOMIZER_SYNTAX = AdErrorEnum.AdError.V(143)
    UNSUPPORTED_AD_CUSTOMIZER_SYNTAX = AdErrorEnum.AdError.V(144)
    UNPAIRED_BRACE_IN_AD_CUSTOMIZER_TAG = AdErrorEnum.AdError.V(145)
    MORE_THAN_ONE_COUNTDOWN_TAG_TYPE_EXISTS = AdErrorEnum.AdError.V(146)
    DATE_TIME_IN_COUNTDOWN_TAG_IS_INVALID = AdErrorEnum.AdError.V(147)
    DATE_TIME_IN_COUNTDOWN_TAG_IS_PAST = AdErrorEnum.AdError.V(148)
    UNRECOGNIZED_AD_CUSTOMIZER_TAG_FOUND = AdErrorEnum.AdError.V(149)
    def __init__(
        self,
    ) -> None: ...

global___AdErrorEnum = AdErrorEnum

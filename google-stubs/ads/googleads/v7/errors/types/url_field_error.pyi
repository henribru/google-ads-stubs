from typing import Any

import proto

__protobuf__: Any

class UrlFieldErrorEnum(proto.Message):
    class UrlFieldError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_TRACKING_URL_TEMPLATE: int
        INVALID_TAG_IN_TRACKING_URL_TEMPLATE: int
        MISSING_TRACKING_URL_TEMPLATE_TAG: int
        MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE: int
        INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE: int
        MALFORMED_TRACKING_URL_TEMPLATE: int
        MISSING_HOST_IN_TRACKING_URL_TEMPLATE: int
        INVALID_TLD_IN_TRACKING_URL_TEMPLATE: int
        REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG: int
        INVALID_FINAL_URL: int
        INVALID_TAG_IN_FINAL_URL: int
        REDUNDANT_NESTED_FINAL_URL_TAG: int
        MISSING_PROTOCOL_IN_FINAL_URL: int
        INVALID_PROTOCOL_IN_FINAL_URL: int
        MALFORMED_FINAL_URL: int
        MISSING_HOST_IN_FINAL_URL: int
        INVALID_TLD_IN_FINAL_URL: int
        INVALID_FINAL_MOBILE_URL: int
        INVALID_TAG_IN_FINAL_MOBILE_URL: int
        REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG: int
        MISSING_PROTOCOL_IN_FINAL_MOBILE_URL: int
        INVALID_PROTOCOL_IN_FINAL_MOBILE_URL: int
        MALFORMED_FINAL_MOBILE_URL: int
        MISSING_HOST_IN_FINAL_MOBILE_URL: int
        INVALID_TLD_IN_FINAL_MOBILE_URL: int
        INVALID_FINAL_APP_URL: int
        INVALID_TAG_IN_FINAL_APP_URL: int
        REDUNDANT_NESTED_FINAL_APP_URL_TAG: int
        MULTIPLE_APP_URLS_FOR_OSTYPE: int
        INVALID_OSTYPE: int
        INVALID_PROTOCOL_FOR_APP_URL: int
        INVALID_PACKAGE_ID_FOR_APP_URL: int
        URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT: int
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY: int
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE: int
        INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE: int
        REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG: int
        MISSING_PROTOCOL: int
        INVALID_PROTOCOL: int
        INVALID_URL: int
        DESTINATION_URL_DEPRECATED: int
        INVALID_TAG_IN_URL: int
        MISSING_URL_TAG: int
        DUPLICATE_URL_ID: int
        INVALID_URL_ID: int
        FINAL_URL_SUFFIX_MALFORMED: int
        INVALID_TAG_IN_FINAL_URL_SUFFIX: int
        INVALID_TOP_LEVEL_DOMAIN: int
        MALFORMED_TOP_LEVEL_DOMAIN: int
        MALFORMED_URL: int
        MISSING_HOST: int
        NULL_CUSTOM_PARAMETER_VALUE: int

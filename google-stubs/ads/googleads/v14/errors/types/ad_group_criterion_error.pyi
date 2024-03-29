from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdGroupCriterionErrorEnum(proto.Message):
    class AdGroupCriterionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST = 2
        AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS = 3
        CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION = 4
        TOO_MANY_OPERATIONS = 5
        CANT_UPDATE_NEGATIVE = 6
        CONCRETE_TYPE_REQUIRED = 7
        BID_INCOMPATIBLE_WITH_ADGROUP = 8
        CANNOT_TARGET_AND_EXCLUDE = 9
        ILLEGAL_URL = 10
        INVALID_KEYWORD_TEXT = 11
        INVALID_DESTINATION_URL = 12
        MISSING_DESTINATION_URL_TAG = 13
        KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM = 14
        INVALID_USER_STATUS = 15
        CANNOT_ADD_CRITERIA_TYPE = 16
        CANNOT_EXCLUDE_CRITERIA_TYPE = 17
        CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE = 27
        OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS = 28
        CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS = 29
        CANNOT_SET_WITHOUT_FINAL_URLS = 30
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST = 31
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST = 32
        CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS = 33
        CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST = 34
        CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS = 35
        CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE = 36
        FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = 37
        FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = 38

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

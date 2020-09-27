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

class AdGroupCriterionErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AdGroupCriterionErrorValue = typing___NewType(
        "AdGroupCriterionErrorValue", builtin___int
    )
    type___AdGroupCriterionErrorValue = AdGroupCriterionErrorValue
    AdGroupCriterionError: _AdGroupCriterionError
    class _AdGroupCriterionError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 0
        )
        UNKNOWN = typing___cast(AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 1)
        AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 2
        )
        AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 3
        )
        CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 4
        )
        TOO_MANY_OPERATIONS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 5
        )
        CANT_UPDATE_NEGATIVE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 6
        )
        CONCRETE_TYPE_REQUIRED = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 7
        )
        BID_INCOMPATIBLE_WITH_ADGROUP = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 8
        )
        CANNOT_TARGET_AND_EXCLUDE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 9
        )
        ILLEGAL_URL = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 10
        )
        INVALID_KEYWORD_TEXT = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 11
        )
        INVALID_DESTINATION_URL = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 12
        )
        MISSING_DESTINATION_URL_TAG = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 13
        )
        KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 14
        )
        INVALID_USER_STATUS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 15
        )
        CANNOT_ADD_CRITERIA_TYPE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 16
        )
        CANNOT_EXCLUDE_CRITERIA_TYPE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 17
        )
        CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 27
        )
        OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 28
        )
        CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 29
        )
        CANNOT_SET_WITHOUT_FINAL_URLS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 30
        )
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 31
        )
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 32
        )
        CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 33
        )
        CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 34
        )
        CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 35
        )
        CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 36
        )
        FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 37
        )
        FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
            AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 38
        )
    UNSPECIFIED = typing___cast(AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 0)
    UNKNOWN = typing___cast(AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 1)
    AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 2
    )
    AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 3
    )
    CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 4
    )
    TOO_MANY_OPERATIONS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 5
    )
    CANT_UPDATE_NEGATIVE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 6
    )
    CONCRETE_TYPE_REQUIRED = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 7
    )
    BID_INCOMPATIBLE_WITH_ADGROUP = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 8
    )
    CANNOT_TARGET_AND_EXCLUDE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 9
    )
    ILLEGAL_URL = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 10
    )
    INVALID_KEYWORD_TEXT = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 11
    )
    INVALID_DESTINATION_URL = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 12
    )
    MISSING_DESTINATION_URL_TAG = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 13
    )
    KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 14
    )
    INVALID_USER_STATUS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 15
    )
    CANNOT_ADD_CRITERIA_TYPE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 16
    )
    CANNOT_EXCLUDE_CRITERIA_TYPE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 17
    )
    CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 27
    )
    OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 28
    )
    CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 29
    )
    CANNOT_SET_WITHOUT_FINAL_URLS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 30
    )
    CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 31
    )
    CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 32
    )
    CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 33
    )
    CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 34
    )
    CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 35
    )
    CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 36
    )
    FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 37
    )
    FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE = typing___cast(
        AdGroupCriterionErrorEnum.AdGroupCriterionErrorValue, 38
    )
    type___AdGroupCriterionError = AdGroupCriterionError
    def __init__(self,) -> None: ...

type___AdGroupCriterionErrorEnum = AdGroupCriterionErrorEnum
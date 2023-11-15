from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ConversionUploadErrorEnum(proto.Message):
    class ConversionUploadError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_MANY_CONVERSIONS_IN_REQUEST = 2
        UNPARSEABLE_GCLID = 3
        CONVERSION_PRECEDES_EVENT = 42
        EXPIRED_EVENT = 43
        TOO_RECENT_EVENT = 44
        EVENT_NOT_FOUND = 45
        UNAUTHORIZED_CUSTOMER = 8
        TOO_RECENT_CONVERSION_ACTION = 10
        CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME = 11
        EXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION = (
            12
        )
        EXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION = (
            13
        )
        ORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION = 14
        ORDER_ID_ALREADY_IN_USE = 15
        DUPLICATE_ORDER_ID = 16
        TOO_RECENT_CALL = 17
        EXPIRED_CALL = 18
        CALL_NOT_FOUND = 19
        CONVERSION_PRECEDES_CALL = 20
        CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME = 21
        UNPARSEABLE_CALLERS_PHONE_NUMBER = 22
        CLICK_CONVERSION_ALREADY_EXISTS = 23
        CALL_CONVERSION_ALREADY_EXISTS = 24
        DUPLICATE_CLICK_CONVERSION_IN_REQUEST = 25
        DUPLICATE_CALL_CONVERSION_IN_REQUEST = 26
        CUSTOM_VARIABLE_NOT_ENABLED = 28
        CUSTOM_VARIABLE_VALUE_CONTAINS_PII = 29
        INVALID_CUSTOMER_FOR_CLICK = 30
        INVALID_CUSTOMER_FOR_CALL = 31
        CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY = 32
        CLICK_NOT_FOUND = 33
        INVALID_USER_IDENTIFIER = 34
        EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER = 35
        UNSUPPORTED_USER_IDENTIFIER = 36
        GBRAID_WBRAID_BOTH_SET = 38
        UNPARSEABLE_WBRAID = 39
        UNPARSEABLE_GBRAID = 40
        ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID = 46
        CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS = 47
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS = 48
        ORDER_ID_CONTAINS_PII = 49
        CUSTOMER_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS = 50
        INVALID_JOB_ID = 52
        NO_CONVERSION_ACTION_FOUND = 53
        INVALID_CONVERSION_ACTION_TYPE = 54
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...

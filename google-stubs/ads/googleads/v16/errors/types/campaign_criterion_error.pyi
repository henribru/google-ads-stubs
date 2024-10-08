from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignCriterionErrorEnum(proto.Message):
    class CampaignCriterionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONCRETE_TYPE_REQUIRED = 2
        INVALID_PLACEMENT_URL = 3
        CANNOT_EXCLUDE_CRITERIA_TYPE = 4
        CANNOT_SET_STATUS_FOR_CRITERIA_TYPE = 5
        CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA = 6
        CANNOT_TARGET_AND_EXCLUDE = 7
        TOO_MANY_OPERATIONS = 8
        OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE = 9
        SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL = 10
        CANNOT_ADD_EXISTING_FIELD = 11
        CANNOT_UPDATE_NEGATIVE_CRITERION = 12
        CANNOT_SET_NEGATIVE_KEYWORD_THEME_CONSTANT_CRITERION = 13
        INVALID_KEYWORD_THEME_CONSTANT = 14
        MISSING_KEYWORD_THEME_CONSTANT_OR_FREE_FORM_KEYWORD_THEME = 15
        CANNOT_TARGET_BOTH_PROXIMITY_AND_LOCATION_CRITERIA_FOR_SMART_CAMPAIGN = 16
        CANNOT_TARGET_MULTIPLE_PROXIMITY_CRITERIA_FOR_SMART_CAMPAIGN = 17
        LOCATION_NOT_LAUNCHED_FOR_LOCAL_SERVICES_CAMPAIGN = 18
        LOCATION_INVALID_FOR_LOCAL_SERVICES_CAMPAIGN = 19
        CANNOT_TARGET_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN = 20
        LOCATION_NOT_IN_HOME_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN = 21
        CANNOT_ADD_OR_REMOVE_LOCATION_FOR_LOCAL_SERVICES_CAMPAIGN = 22
        AT_LEAST_ONE_POSITIVE_LOCATION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN = 23
        AT_LEAST_ONE_LOCAL_SERVICE_ID_CRITERION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN = (
            24
        )
        LOCAL_SERVICE_ID_NOT_FOUND_FOR_CATEGORY = 25
        CANNOT_ATTACH_BRAND_LIST_TO_NON_QUALIFIED_SEARCH_CAMPAIGN = 26
        CANNOT_REMOVE_ALL_LOCATIONS_DUE_TO_TOO_MANY_COUNTRY_EXCLUSIONS = 27

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

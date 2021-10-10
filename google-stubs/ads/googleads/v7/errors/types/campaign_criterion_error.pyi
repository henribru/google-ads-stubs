from typing import Any

import proto

__protobuf__: Any

class CampaignCriterionErrorEnum(proto.Message):
    class CampaignCriterionError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONCRETE_TYPE_REQUIRED: int
        INVALID_PLACEMENT_URL: int
        CANNOT_EXCLUDE_CRITERIA_TYPE: int
        CANNOT_SET_STATUS_FOR_CRITERIA_TYPE: int
        CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA: int
        CANNOT_TARGET_AND_EXCLUDE: int
        TOO_MANY_OPERATIONS: int
        OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE: int
        SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL: int
        CANNOT_ADD_EXISTING_FIELD: int
        CANNOT_UPDATE_NEGATIVE_CRITERION: int

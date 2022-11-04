from typing import Any

import proto

class SmartCampaignErrorEnum(proto.Message):
    class SmartCampaignError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_BUSINESS_LOCATION_ID = 2
        INVALID_CAMPAIGN = 3
        BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING = 4
        REQUIRED_SUGGESTION_FIELD_MISSING = 5
        GEO_TARGETS_REQUIRED = 6
        CANNOT_DETERMINE_SUGGESTION_LOCALE = 7
        FINAL_URL_NOT_CRAWLABLE = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

class SmartCampaignNotEligibleReasonEnum(proto.Message):
    class SmartCampaignNotEligibleReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNT_ISSUE = 2
        BILLING_ISSUE = 3
        BUSINESS_PROFILE_LOCATION_REMOVED = 4
        ALL_ADS_DISAPPROVED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

__protobuf__: Any

class CampaignDraftErrorEnum(proto.Message):
    class CampaignDraftError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_DRAFT_NAME: int
        INVALID_STATUS_TRANSITION_FROM_REMOVED: int
        INVALID_STATUS_TRANSITION_FROM_PROMOTED: int
        INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED: int
        CUSTOMER_CANNOT_CREATE_DRAFT: int
        CAMPAIGN_CANNOT_CREATE_DRAFT: int
        INVALID_DRAFT_CHANGE: int
        INVALID_STATUS_TRANSITION: int
        MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED: int
        LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY: int

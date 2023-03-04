from typing import Any

import proto

class CampaignExperimentErrorEnum(proto.Message):
    class CampaignExperimentError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        INVALID_TRANSITION = 3
        CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET = 4
        CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN = 5
        CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT = 6
        CUSTOMER_CANNOT_CREATE_EXPERIMENT = 7
        CAMPAIGN_CANNOT_CREATE_EXPERIMENT = 8
        EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP = 9
        EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION = 10
        CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS = 11
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...

from typing import Any

import proto

from google.ads.googleads.v10.enums.types.campaign_draft_status import (
    CampaignDraftStatusEnum,
)

class CampaignDraft(proto.Message):
    resource_name: str
    draft_id: int
    base_campaign: str
    name: str
    draft_campaign: str
    status: CampaignDraftStatusEnum.CampaignDraftStatus
    has_experiment_running: bool
    long_running_operation: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        draft_id: int = ...,
        base_campaign: str = ...,
        name: str = ...,
        draft_campaign: str = ...,
        status: CampaignDraftStatusEnum.CampaignDraftStatus = ...,
        has_experiment_running: bool = ...,
        long_running_operation: str = ...
    ) -> None: ...

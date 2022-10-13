from typing import Any

import proto

from google.ads.googleads.v11.enums.types.campaign_shared_set_status import (
    CampaignSharedSetStatusEnum,
)

class CampaignSharedSet(proto.Message):
    resource_name: str
    campaign: str
    shared_set: str
    status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        shared_set: str = ...,
        status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus = ...
    ) -> None: ...

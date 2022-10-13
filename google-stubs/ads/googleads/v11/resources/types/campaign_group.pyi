from typing import Any

import proto

from google.ads.googleads.v11.enums.types.campaign_group_status import (
    CampaignGroupStatusEnum,
)

class CampaignGroup(proto.Message):
    resource_name: str
    id: int
    name: str
    status: CampaignGroupStatusEnum.CampaignGroupStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: CampaignGroupStatusEnum.CampaignGroupStatus = ...
    ) -> None: ...

from typing import Any

import proto

class CampaignSearchTermInsight(proto.Message):
    resource_name: str
    category_label: str
    id: int
    campaign_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        category_label: str = ...,
        id: int = ...,
        campaign_id: int = ...
    ) -> None: ...

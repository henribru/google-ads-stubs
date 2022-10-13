from typing import Any

import proto

class SmartCampaignSearchTermView(proto.Message):
    resource_name: str
    search_term: str
    campaign: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        search_term: str = ...,
        campaign: str = ...
    ) -> None: ...

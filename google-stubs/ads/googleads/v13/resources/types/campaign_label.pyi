from typing import Any

import proto

class CampaignLabel(proto.Message):
    resource_name: str
    campaign: str
    label: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        label: str = ...
    ) -> None: ...

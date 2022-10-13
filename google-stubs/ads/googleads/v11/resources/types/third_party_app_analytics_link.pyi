from typing import Any

import proto

class ThirdPartyAppAnalyticsLink(proto.Message):
    resource_name: str
    shareable_link_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        shareable_link_id: str = ...
    ) -> None: ...

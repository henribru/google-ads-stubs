from typing import Any

import proto

from google.ads.googleads.v11.enums.types.combined_audience_status import (
    CombinedAudienceStatusEnum,
)

class CombinedAudience(proto.Message):
    resource_name: str
    id: int
    status: CombinedAudienceStatusEnum.CombinedAudienceStatus
    name: str
    description: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        status: CombinedAudienceStatusEnum.CombinedAudienceStatus = ...,
        name: str = ...,
        description: str = ...
    ) -> None: ...

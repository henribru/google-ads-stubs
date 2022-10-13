from typing import Any

import proto

from google.ads.googleads.v10.common.types.audiences import (
    AudienceDimension,
    AudienceExclusionDimension,
)
from google.ads.googleads.v10.enums.types.audience_status import AudienceStatusEnum

class Audience(proto.Message):
    resource_name: str
    id: int
    status: AudienceStatusEnum.AudienceStatus
    name: str
    description: str
    dimensions: list[AudienceDimension]
    exclusion_dimension: AudienceExclusionDimension
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        status: AudienceStatusEnum.AudienceStatus = ...,
        name: str = ...,
        description: str = ...,
        dimensions: list[AudienceDimension] = ...,
        exclusion_dimension: AudienceExclusionDimension = ...
    ) -> None: ...

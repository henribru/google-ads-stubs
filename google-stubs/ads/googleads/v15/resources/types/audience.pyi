from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.common.types.audiences import (
    AudienceDimension,
    AudienceExclusionDimension,
)
from google.ads.googleads.v15.enums.types.audience_scope import AudienceScopeEnum
from google.ads.googleads.v15.enums.types.audience_status import AudienceStatusEnum

class Audience(proto.Message):
    resource_name: str
    id: int
    status: AudienceStatusEnum.AudienceStatus
    name: str
    description: str
    dimensions: MutableSequence[AudienceDimension]
    exclusion_dimension: AudienceExclusionDimension
    scope: AudienceScopeEnum.AudienceScope
    asset_group: str
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
        dimensions: MutableSequence[AudienceDimension] = ...,
        exclusion_dimension: AudienceExclusionDimension = ...,
        scope: AudienceScopeEnum.AudienceScope = ...,
        asset_group: str = ...
    ) -> None: ...

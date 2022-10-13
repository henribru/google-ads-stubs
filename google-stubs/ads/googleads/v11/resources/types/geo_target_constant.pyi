from typing import Any

import proto

from google.ads.googleads.v11.enums.types.geo_target_constant_status import (
    GeoTargetConstantStatusEnum,
)

class GeoTargetConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    country_code: str
    target_type: str
    status: GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    canonical_name: str
    parent_geo_target: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        country_code: str = ...,
        target_type: str = ...,
        status: GeoTargetConstantStatusEnum.GeoTargetConstantStatus = ...,
        canonical_name: str = ...,
        parent_geo_target: str = ...
    ) -> None: ...

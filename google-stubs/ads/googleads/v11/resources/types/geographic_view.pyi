from typing import Any

import proto

from google.ads.googleads.v11.enums.types.geo_targeting_type import GeoTargetingTypeEnum

class GeographicView(proto.Message):
    resource_name: str
    location_type: GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        location_type: GeoTargetingTypeEnum.GeoTargetingType = ...,
        country_criterion_id: int = ...
    ) -> None: ...

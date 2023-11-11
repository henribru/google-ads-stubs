from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.geo_targeting_type import GeoTargetingTypeEnum

_M = TypeVar("_M")

class GeographicView(proto.Message):
    resource_name: str
    location_type: GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        location_type: GeoTargetingTypeEnum.GeoTargetingType = ...,
        country_criterion_id: int = ...
    ) -> None: ...

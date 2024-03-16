from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.geo_targeting_type import GeoTargetingTypeEnum

_M = TypeVar("_M")

class GeographicView(proto.Message):
    resource_name: str
    location_type: GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        location_type: GeoTargetingTypeEnum.GeoTargetingType = ...,
        country_criterion_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "location_type", "country_criterion_id"]
    ) -> bool: ...

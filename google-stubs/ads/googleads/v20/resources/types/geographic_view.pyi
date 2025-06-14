from google.ads.googleads.v20.enums.types.geo_targeting_type import GeoTargetingTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class GeographicView(proto.Message):
    resource_name: str
    location_type: GeoTargetingTypeEnum.GeoTargetingType
    country_criterion_id: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., location_type: GeoTargetingTypeEnum.GeoTargetingType = ..., country_criterion_id: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "location_type", "country_criterion_id"]) -> bool: ...

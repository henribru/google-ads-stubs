from google.ads.googleads.v22.enums.types.placement_type import PlacementTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class DetailContentSuitabilityPlacementView(proto.Message):
    resource_name: str
    display_name: str
    placement: str
    placement_type: PlacementTypeEnum.PlacementType
    target_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., display_name: str = ..., placement: str = ..., placement_type: PlacementTypeEnum.PlacementType = ..., target_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "display_name", "placement", "placement_type", "target_url"]) -> bool: ...

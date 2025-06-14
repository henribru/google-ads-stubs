from google.ads.googleads.v20.enums.types.placement_type import PlacementTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class GroupPlacementView(proto.Message):
    resource_name: str
    placement: str
    display_name: str
    target_url: str
    placement_type: PlacementTypeEnum.PlacementType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., placement: str = ..., display_name: str = ..., target_url: str = ..., placement_type: PlacementTypeEnum.PlacementType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "placement", "display_name", "target_url", "placement_type"]) -> bool: ...

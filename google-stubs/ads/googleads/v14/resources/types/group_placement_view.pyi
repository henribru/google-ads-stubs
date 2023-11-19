from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.placement_type import PlacementTypeEnum

_M = TypeVar("_M")

class GroupPlacementView(proto.Message):
    resource_name: str
    placement: str
    display_name: str
    target_url: str
    placement_type: PlacementTypeEnum.PlacementType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        placement: str = ...,
        display_name: str = ...,
        target_url: str = ...,
        placement_type: PlacementTypeEnum.PlacementType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "placement", "display_name", "target_url", "placement_type"]) -> bool: ...  # type: ignore[override]

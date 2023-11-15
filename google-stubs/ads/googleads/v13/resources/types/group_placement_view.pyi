from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.placement_type import PlacementTypeEnum

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

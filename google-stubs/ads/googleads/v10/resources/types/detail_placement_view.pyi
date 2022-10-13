from typing import Any

import proto

from google.ads.googleads.v10.enums.types.placement_type import PlacementTypeEnum

class DetailPlacementView(proto.Message):
    resource_name: str
    placement: str
    display_name: str
    group_placement_target_url: str
    target_url: str
    placement_type: PlacementTypeEnum.PlacementType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        placement: str = ...,
        display_name: str = ...,
        group_placement_target_url: str = ...,
        target_url: str = ...,
        placement_type: PlacementTypeEnum.PlacementType = ...
    ) -> None: ...

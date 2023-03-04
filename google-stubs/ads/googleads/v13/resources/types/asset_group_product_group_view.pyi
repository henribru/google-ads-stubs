from typing import Any

import proto

class AssetGroupProductGroupView(proto.Message):
    resource_name: str
    asset_group: str
    asset_group_listing_group_filter: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group: str = ...,
        asset_group_listing_group_filter: str = ...
    ) -> None: ...

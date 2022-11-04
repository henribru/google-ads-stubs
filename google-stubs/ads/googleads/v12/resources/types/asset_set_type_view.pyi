from typing import Any

import proto

from google.ads.googleads.v12.enums.types.asset_set_type import AssetSetTypeEnum

class AssetSetTypeView(proto.Message):
    resource_name: str
    asset_set_type: AssetSetTypeEnum.AssetSetType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set_type: AssetSetTypeEnum.AssetSetType = ...
    ) -> None: ...

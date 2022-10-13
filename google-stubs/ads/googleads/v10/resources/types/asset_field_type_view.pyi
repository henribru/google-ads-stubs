from typing import Any

import proto

from google.ads.googleads.v10.enums.types.asset_field_type import AssetFieldTypeEnum

class AssetFieldTypeView(proto.Message):
    resource_name: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...
    ) -> None: ...

from typing import Any

import proto

from google.ads.googleads.v10.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v10.enums.types.asset_link_status import AssetLinkStatusEnum

class CustomerAsset(proto.Message):
    resource_name: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    status: AssetLinkStatusEnum.AssetLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...
    ) -> None: ...

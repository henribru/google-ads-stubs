from typing import Any

import proto

from google.ads.googleads.v12.enums.types.asset_set_link_status import (
    AssetSetLinkStatusEnum,
)

class CustomerAssetSet(proto.Message):
    resource_name: str
    asset_set: str
    customer: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_set: str = ...,
        customer: str = ...,
        status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...
    ) -> None: ...

from typing import Any

import proto

from google.ads.googleads.v10.enums.types.asset_set_link_status import (
    AssetSetLinkStatusEnum,
)

class CampaignAssetSet(proto.Message):
    resource_name: str
    campaign: str
    asset_set: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        asset_set: str = ...,
        status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...
    ) -> None: ...

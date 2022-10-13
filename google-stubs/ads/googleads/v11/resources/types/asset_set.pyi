from typing import Any

import proto

from google.ads.googleads.v11.enums.types.asset_set_status import AssetSetStatusEnum
from google.ads.googleads.v11.enums.types.asset_set_type import AssetSetTypeEnum

class AssetSet(proto.Message):
    class MerchantCenterFeed(proto.Message):
        merchant_id: int
        feed_label: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            merchant_id: int = ...,
            feed_label: str = ...
        ) -> None: ...
    id: int
    resource_name: str
    name: str
    type_: AssetSetTypeEnum.AssetSetType
    status: AssetSetStatusEnum.AssetSetStatus
    merchant_center_feed: AssetSet.MerchantCenterFeed
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        id: int = ...,
        resource_name: str = ...,
        name: str = ...,
        type_: AssetSetTypeEnum.AssetSetType = ...,
        status: AssetSetStatusEnum.AssetSetStatus = ...,
        merchant_center_feed: AssetSet.MerchantCenterFeed = ...
    ) -> None: ...

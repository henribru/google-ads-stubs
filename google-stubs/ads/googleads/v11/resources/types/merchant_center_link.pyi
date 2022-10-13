from typing import Any

import proto

from google.ads.googleads.v11.enums.types.merchant_center_link_status import (
    MerchantCenterLinkStatusEnum,
)

class MerchantCenterLink(proto.Message):
    resource_name: str
    id: int
    merchant_center_account_name: str
    status: MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        merchant_center_account_name: str = ...,
        status: MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus = ...
    ) -> None: ...

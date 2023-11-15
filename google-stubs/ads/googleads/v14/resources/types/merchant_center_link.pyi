from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.merchant_center_link_status import (
    MerchantCenterLinkStatusEnum,
)

_M = TypeVar("_M")

class MerchantCenterLink(proto.Message):
    resource_name: str
    id: int
    merchant_center_account_name: str
    status: MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        merchant_center_account_name: str = ...,
        status: MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus = ...
    ) -> None: ...

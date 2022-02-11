from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    merchant_center_link_status as merchant_center_link_status,
)

__protobuf__: Any

class MerchantCenterLink(proto.Message):
    resource_name: Any
    id: Any
    merchant_center_account_name: Any
    status: Any

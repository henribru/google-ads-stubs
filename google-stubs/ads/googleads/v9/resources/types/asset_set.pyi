from typing import Any

import proto

from google.ads.googleads.v9.enums.types import (
    asset_set_status as asset_set_status,
    asset_set_type as asset_set_type,
)

__protobuf__: Any

class AssetSet(proto.Message):
    class MerchantCenterFeed(proto.Message):
        merchant_id: Any
        feed_label: Any
    resource_name: Any
    name: Any
    type_: Any
    status: Any
    merchant_center_feed: Any

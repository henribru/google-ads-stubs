import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    asset_set_status as asset_set_status,
    asset_set_type as asset_set_type,
)

__protobuf__: Incomplete

class AssetSet(proto.Message):
    class MerchantCenterFeed(proto.Message):
        merchant_id: Incomplete
        feed_label: Incomplete
    id: Incomplete
    resource_name: Incomplete
    name: Incomplete
    type_: Incomplete
    status: Incomplete
    merchant_center_feed: Incomplete

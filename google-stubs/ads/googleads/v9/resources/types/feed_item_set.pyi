from typing import Any

import proto

from google.ads.googleads.v9.common.types import (
    feed_item_set_filter_type_infos as feed_item_set_filter_type_infos,
)
from google.ads.googleads.v9.enums.types import (
    feed_item_set_status as feed_item_set_status,
)

__protobuf__: Any

class FeedItemSet(proto.Message):
    resource_name: Any
    feed: Any
    feed_item_set_id: Any
    display_name: Any
    status: Any
    dynamic_location_set_filter: Any
    dynamic_affiliate_location_set_filter: Any

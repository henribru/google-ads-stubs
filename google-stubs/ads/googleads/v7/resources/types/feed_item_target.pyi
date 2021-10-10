from typing import Any

import proto

from google.ads.googleads.v7.common.types import criteria as criteria
from google.ads.googleads.v7.enums.types import (
    feed_item_target_device as feed_item_target_device,
    feed_item_target_status as feed_item_target_status,
)

__protobuf__: Any

class FeedItemTarget(proto.Message):
    resource_name: Any
    feed_item: Any
    feed_item_target_type: Any
    feed_item_target_id: Any
    status: Any
    campaign: Any
    ad_group: Any
    keyword: Any
    geo_target_constant: Any
    device: Any
    ad_schedule: Any

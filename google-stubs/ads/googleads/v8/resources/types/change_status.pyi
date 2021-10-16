from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    change_status_operation as change_status_operation,
    change_status_resource_type as change_status_resource_type,
)

__protobuf__: Any

class ChangeStatus(proto.Message):
    resource_name: Any
    last_change_date_time: Any
    resource_type: Any
    campaign: Any
    ad_group: Any
    resource_status: Any
    ad_group_ad: Any
    ad_group_criterion: Any
    campaign_criterion: Any
    feed: Any
    feed_item: Any
    ad_group_feed: Any
    campaign_feed: Any
    ad_group_bid_modifier: Any
    shared_set: Any
    campaign_shared_set: Any
    asset: Any
    customer_asset: Any
    campaign_asset: Any
    ad_group_asset: Any

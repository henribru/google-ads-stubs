from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v9.enums.types import (
    change_client_type as change_client_type,
    change_event_resource_type as change_event_resource_type,
)

__protobuf__: Any

class ChangeEvent(proto.Message):
    class ChangedResource(proto.Message):
        ad: Any
        ad_group: Any
        ad_group_criterion: Any
        campaign: Any
        campaign_budget: Any
        ad_group_bid_modifier: Any
        campaign_criterion: Any
        feed: Any
        feed_item: Any
        campaign_feed: Any
        ad_group_feed: Any
        ad_group_ad: Any
        asset: Any
        customer_asset: Any
        campaign_asset: Any
        ad_group_asset: Any
    resource_name: Any
    change_date_time: Any
    change_resource_type: Any
    change_resource_name: Any
    client_type: Any
    user_email: Any
    old_resource: Any
    new_resource: Any
    resource_change_operation: Any
    changed_fields: Any
    campaign: Any
    ad_group: Any
    feed: Any
    feed_item: Any
    asset: Any

import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v11.enums.types import (
    change_client_type as change_client_type,
    change_event_resource_type as change_event_resource_type,
)

__protobuf__: Incomplete

class ChangeEvent(proto.Message):
    class ChangedResource(proto.Message):
        ad: Incomplete
        ad_group: Incomplete
        ad_group_criterion: Incomplete
        campaign: Incomplete
        campaign_budget: Incomplete
        ad_group_bid_modifier: Incomplete
        campaign_criterion: Incomplete
        feed: Incomplete
        feed_item: Incomplete
        campaign_feed: Incomplete
        ad_group_feed: Incomplete
        ad_group_ad: Incomplete
        asset: Incomplete
        customer_asset: Incomplete
        campaign_asset: Incomplete
        ad_group_asset: Incomplete
        asset_set: Incomplete
        asset_set_asset: Incomplete
        campaign_asset_set: Incomplete
    resource_name: Incomplete
    change_date_time: Incomplete
    change_resource_type: Incomplete
    change_resource_name: Incomplete
    client_type: Incomplete
    user_email: Incomplete
    old_resource: Incomplete
    new_resource: Incomplete
    resource_change_operation: Incomplete
    changed_fields: Incomplete
    campaign: Incomplete
    ad_group: Incomplete
    feed: Incomplete
    feed_item: Incomplete
    asset: Incomplete

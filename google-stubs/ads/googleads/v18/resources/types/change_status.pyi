import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import change_status_operation, change_status_resource_type

__protobuf__: Incomplete

class ChangeStatus(proto.Message):
    resource_name: str
    last_change_date_time: str
    resource_type: change_status_resource_type.ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    campaign: str
    ad_group: str
    resource_status: change_status_operation.ChangeStatusOperationEnum.ChangeStatusOperation
    ad_group_ad: str
    ad_group_criterion: str
    campaign_criterion: str
    feed: str
    feed_item: str
    ad_group_feed: str
    campaign_feed: str
    ad_group_bid_modifier: str
    shared_set: str
    campaign_shared_set: str
    asset: str
    customer_asset: str
    campaign_asset: str
    ad_group_asset: str
    combined_audience: str
    asset_group: str

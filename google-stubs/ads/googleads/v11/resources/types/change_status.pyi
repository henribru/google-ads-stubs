from typing import Any

import proto

from google.ads.googleads.v11.enums.types.change_status_operation import (
    ChangeStatusOperationEnum,
)
from google.ads.googleads.v11.enums.types.change_status_resource_type import (
    ChangeStatusResourceTypeEnum,
)

class ChangeStatus(proto.Message):
    resource_name: str
    last_change_date_time: str
    resource_type: ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    campaign: str
    ad_group: str
    resource_status: ChangeStatusOperationEnum.ChangeStatusOperation
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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        last_change_date_time: str = ...,
        resource_type: ChangeStatusResourceTypeEnum.ChangeStatusResourceType = ...,
        campaign: str = ...,
        ad_group: str = ...,
        resource_status: ChangeStatusOperationEnum.ChangeStatusOperation = ...,
        ad_group_ad: str = ...,
        ad_group_criterion: str = ...,
        campaign_criterion: str = ...,
        feed: str = ...,
        feed_item: str = ...,
        ad_group_feed: str = ...,
        campaign_feed: str = ...,
        ad_group_bid_modifier: str = ...,
        shared_set: str = ...,
        campaign_shared_set: str = ...,
        asset: str = ...,
        customer_asset: str = ...,
        campaign_asset: str = ...,
        ad_group_asset: str = ...
    ) -> None: ...

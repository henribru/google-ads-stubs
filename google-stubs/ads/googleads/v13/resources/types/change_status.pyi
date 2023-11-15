from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.change_status_operation import (
    ChangeStatusOperationEnum,
)
from google.ads.googleads.v13.enums.types.change_status_resource_type import (
    ChangeStatusResourceTypeEnum,
)

_M = TypeVar("_M")

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
    combined_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        ad_group_asset: str = ...,
        combined_audience: str = ...
    ) -> None: ...

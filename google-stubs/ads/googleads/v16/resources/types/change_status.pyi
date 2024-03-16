from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.change_status_operation import (
    ChangeStatusOperationEnum,
)
from google.ads.googleads.v16.enums.types.change_status_resource_type import (
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
        combined_audience: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "last_change_date_time",
            "resource_type",
            "campaign",
            "ad_group",
            "resource_status",
            "ad_group_ad",
            "ad_group_criterion",
            "campaign_criterion",
            "feed",
            "feed_item",
            "ad_group_feed",
            "campaign_feed",
            "ad_group_bid_modifier",
            "shared_set",
            "campaign_shared_set",
            "asset",
            "customer_asset",
            "campaign_asset",
            "ad_group_asset",
            "combined_audience",
        ],
    ) -> bool: ...

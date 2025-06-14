from google.ads.googleads.v19.enums.types.change_status_operation import ChangeStatusOperationEnum
from google.ads.googleads.v19.enums.types.change_status_resource_type import ChangeStatusResourceTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    ad_group_bid_modifier: str
    shared_set: str
    campaign_shared_set: str
    asset: str
    customer_asset: str
    campaign_asset: str
    ad_group_asset: str
    combined_audience: str
    asset_group: str
    campaign_budget: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., last_change_date_time: str = ..., resource_type: ChangeStatusResourceTypeEnum.ChangeStatusResourceType = ..., campaign: str = ..., ad_group: str = ..., resource_status: ChangeStatusOperationEnum.ChangeStatusOperation = ..., ad_group_ad: str = ..., ad_group_criterion: str = ..., campaign_criterion: str = ..., ad_group_bid_modifier: str = ..., shared_set: str = ..., campaign_shared_set: str = ..., asset: str = ..., customer_asset: str = ..., campaign_asset: str = ..., ad_group_asset: str = ..., combined_audience: str = ..., asset_group: str = ..., campaign_budget: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "last_change_date_time", "resource_type", "campaign", "ad_group", "resource_status", "ad_group_ad", "ad_group_criterion", "campaign_criterion", "ad_group_bid_modifier", "shared_set", "campaign_shared_set", "asset", "customer_asset", "campaign_asset", "ad_group_asset", "combined_audience", "asset_group", "campaign_budget"]) -> bool: ...

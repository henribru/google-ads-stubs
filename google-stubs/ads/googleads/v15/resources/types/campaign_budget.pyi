from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.budget_delivery_method import (
    BudgetDeliveryMethodEnum,
)
from google.ads.googleads.v15.enums.types.budget_period import BudgetPeriodEnum
from google.ads.googleads.v15.enums.types.budget_status import BudgetStatusEnum
from google.ads.googleads.v15.enums.types.budget_type import BudgetTypeEnum

_M = TypeVar("_M")

class CampaignBudget(proto.Message):
    resource_name: str
    id: int
    name: str
    amount_micros: int
    total_amount_micros: int
    status: BudgetStatusEnum.BudgetStatus
    delivery_method: BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    explicitly_shared: bool
    reference_count: int
    has_recommended_budget: bool
    recommended_budget_amount_micros: int
    period: BudgetPeriodEnum.BudgetPeriod
    recommended_budget_estimated_change_weekly_clicks: int
    recommended_budget_estimated_change_weekly_cost_micros: int
    recommended_budget_estimated_change_weekly_interactions: int
    recommended_budget_estimated_change_weekly_views: int
    type_: BudgetTypeEnum.BudgetType
    aligned_bidding_strategy_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        amount_micros: int = ...,
        total_amount_micros: int = ...,
        status: BudgetStatusEnum.BudgetStatus = ...,
        delivery_method: BudgetDeliveryMethodEnum.BudgetDeliveryMethod = ...,
        explicitly_shared: bool = ...,
        reference_count: int = ...,
        has_recommended_budget: bool = ...,
        recommended_budget_amount_micros: int = ...,
        period: BudgetPeriodEnum.BudgetPeriod = ...,
        recommended_budget_estimated_change_weekly_clicks: int = ...,
        recommended_budget_estimated_change_weekly_cost_micros: int = ...,
        recommended_budget_estimated_change_weekly_interactions: int = ...,
        recommended_budget_estimated_change_weekly_views: int = ...,
        type_: BudgetTypeEnum.BudgetType = ...,
        aligned_bidding_strategy_id: int = ...
    ) -> None: ...

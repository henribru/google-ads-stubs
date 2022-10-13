from typing import Any

import proto

from google.ads.googleads.v11.enums.types.budget_delivery_method import (
    BudgetDeliveryMethodEnum,
)
from google.ads.googleads.v11.enums.types.budget_period import BudgetPeriodEnum
from google.ads.googleads.v11.enums.types.budget_status import BudgetStatusEnum
from google.ads.googleads.v11.enums.types.budget_type import BudgetTypeEnum

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        type_: BudgetTypeEnum.BudgetType = ...
    ) -> None: ...

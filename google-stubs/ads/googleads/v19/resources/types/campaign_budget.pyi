import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import budget_delivery_method, budget_period, budget_status, budget_type

__protobuf__: Incomplete

class CampaignBudget(proto.Message):
    resource_name: str
    id: int
    name: str
    amount_micros: int
    total_amount_micros: int
    status: budget_status.BudgetStatusEnum.BudgetStatus
    delivery_method: budget_delivery_method.BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    explicitly_shared: bool
    reference_count: int
    has_recommended_budget: bool
    recommended_budget_amount_micros: int
    period: budget_period.BudgetPeriodEnum.BudgetPeriod
    recommended_budget_estimated_change_weekly_clicks: int
    recommended_budget_estimated_change_weekly_cost_micros: int
    recommended_budget_estimated_change_weekly_interactions: int
    recommended_budget_estimated_change_weekly_views: int
    type_: budget_type.BudgetTypeEnum.BudgetType
    aligned_bidding_strategy_id: int

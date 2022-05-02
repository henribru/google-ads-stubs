import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    budget_delivery_method as budget_delivery_method,
    budget_period as budget_period,
    budget_status as budget_status,
    budget_type as budget_type,
)

__protobuf__: Incomplete

class CampaignBudget(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    amount_micros: Incomplete
    total_amount_micros: Incomplete
    status: Incomplete
    delivery_method: Incomplete
    explicitly_shared: Incomplete
    reference_count: Incomplete
    has_recommended_budget: Incomplete
    recommended_budget_amount_micros: Incomplete
    period: Incomplete
    recommended_budget_estimated_change_weekly_clicks: Incomplete
    recommended_budget_estimated_change_weekly_cost_micros: Incomplete
    recommended_budget_estimated_change_weekly_interactions: Incomplete
    recommended_budget_estimated_change_weekly_views: Incomplete
    type_: Incomplete

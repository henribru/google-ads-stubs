from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    budget_delivery_method as budget_delivery_method,
    budget_period as budget_period,
    budget_status as budget_status,
    budget_type as budget_type,
)

__protobuf__: Any

class CampaignBudget(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    amount_micros: Any
    total_amount_micros: Any
    status: Any
    delivery_method: Any
    explicitly_shared: Any
    reference_count: Any
    has_recommended_budget: Any
    recommended_budget_amount_micros: Any
    period: Any
    recommended_budget_estimated_change_weekly_clicks: Any
    recommended_budget_estimated_change_weekly_cost_micros: Any
    recommended_budget_estimated_change_weekly_interactions: Any
    recommended_budget_estimated_change_weekly_views: Any
    type_: Any

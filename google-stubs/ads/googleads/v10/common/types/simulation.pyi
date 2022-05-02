import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BidModifierSimulationPointList(proto.Message):
    points: Incomplete

class CpcBidSimulationPointList(proto.Message):
    points: Incomplete

class CpvBidSimulationPointList(proto.Message):
    points: Incomplete

class TargetCpaSimulationPointList(proto.Message):
    points: Incomplete

class TargetRoasSimulationPointList(proto.Message):
    points: Incomplete

class PercentCpcBidSimulationPointList(proto.Message):
    points: Incomplete

class BudgetSimulationPointList(proto.Message):
    points: Incomplete

class TargetImpressionShareSimulationPointList(proto.Message):
    points: Incomplete

class BidModifierSimulationPoint(proto.Message):
    bid_modifier: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete
    parent_biddable_conversions: Incomplete
    parent_biddable_conversions_value: Incomplete
    parent_clicks: Incomplete
    parent_cost_micros: Incomplete
    parent_impressions: Incomplete
    parent_top_slot_impressions: Incomplete
    parent_required_budget_micros: Incomplete

class CpcBidSimulationPoint(proto.Message):
    required_budget_amount_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete
    cpc_bid_micros: Incomplete
    cpc_bid_scaling_modifier: Incomplete

class CpvBidSimulationPoint(proto.Message):
    cpv_bid_micros: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    views: Incomplete

class TargetCpaSimulationPoint(proto.Message):
    required_budget_amount_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    app_installs: Incomplete
    in_app_actions: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete
    target_cpa_micros: Incomplete
    target_cpa_scaling_modifier: Incomplete

class TargetRoasSimulationPoint(proto.Message):
    target_roas: Incomplete
    required_budget_amount_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete

class PercentCpcBidSimulationPoint(proto.Message):
    percent_cpc_bid_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete

class BudgetSimulationPoint(proto.Message):
    budget_amount_micros: Incomplete
    required_cpc_bid_ceiling_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete

class TargetImpressionShareSimulationPoint(proto.Message):
    target_impression_share_micros: Incomplete
    required_cpc_bid_ceiling_micros: Incomplete
    required_budget_amount_micros: Incomplete
    biddable_conversions: Incomplete
    biddable_conversions_value: Incomplete
    clicks: Incomplete
    cost_micros: Incomplete
    impressions: Incomplete
    top_slot_impressions: Incomplete
    absolute_top_impressions: Incomplete

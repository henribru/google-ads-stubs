from typing import Any

import proto

__protobuf__: Any

class BidModifierSimulationPointList(proto.Message):
    points: Any

class CpcBidSimulationPointList(proto.Message):
    points: Any

class CpvBidSimulationPointList(proto.Message):
    points: Any

class TargetCpaSimulationPointList(proto.Message):
    points: Any

class TargetRoasSimulationPointList(proto.Message):
    points: Any

class PercentCpcBidSimulationPointList(proto.Message):
    points: Any

class BudgetSimulationPointList(proto.Message):
    points: Any

class TargetImpressionShareSimulationPointList(proto.Message):
    points: Any

class BidModifierSimulationPoint(proto.Message):
    bid_modifier: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any
    parent_biddable_conversions: Any
    parent_biddable_conversions_value: Any
    parent_clicks: Any
    parent_cost_micros: Any
    parent_impressions: Any
    parent_top_slot_impressions: Any
    parent_required_budget_micros: Any

class CpcBidSimulationPoint(proto.Message):
    required_budget_amount_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any
    cpc_bid_micros: Any
    cpc_bid_scaling_modifier: Any

class CpvBidSimulationPoint(proto.Message):
    cpv_bid_micros: Any
    cost_micros: Any
    impressions: Any
    views: Any

class TargetCpaSimulationPoint(proto.Message):
    required_budget_amount_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    app_installs: Any
    in_app_actions: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any
    target_cpa_micros: Any
    target_cpa_scaling_modifier: Any

class TargetRoasSimulationPoint(proto.Message):
    target_roas: Any
    required_budget_amount_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any

class PercentCpcBidSimulationPoint(proto.Message):
    percent_cpc_bid_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any

class BudgetSimulationPoint(proto.Message):
    budget_amount_micros: Any
    required_cpc_bid_ceiling_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any

class TargetImpressionShareSimulationPoint(proto.Message):
    target_impression_share_micros: Any
    required_cpc_bid_ceiling_micros: Any
    required_budget_amount_micros: Any
    biddable_conversions: Any
    biddable_conversions_value: Any
    clicks: Any
    cost_micros: Any
    impressions: Any
    top_slot_impressions: Any
    absolute_top_impressions: Any

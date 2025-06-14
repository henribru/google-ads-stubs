import proto
from _typeshed import Incomplete
from typing import MutableSequence

__protobuf__: Incomplete

class CpcBidSimulationPointList(proto.Message):
    points: MutableSequence['CpcBidSimulationPoint']

class CpvBidSimulationPointList(proto.Message):
    points: MutableSequence['CpvBidSimulationPoint']

class TargetCpaSimulationPointList(proto.Message):
    points: MutableSequence['TargetCpaSimulationPoint']

class TargetRoasSimulationPointList(proto.Message):
    points: MutableSequence['TargetRoasSimulationPoint']

class PercentCpcBidSimulationPointList(proto.Message):
    points: MutableSequence['PercentCpcBidSimulationPoint']

class BudgetSimulationPointList(proto.Message):
    points: MutableSequence['BudgetSimulationPoint']

class TargetImpressionShareSimulationPointList(proto.Message):
    points: MutableSequence['TargetImpressionShareSimulationPoint']

class CpcBidSimulationPoint(proto.Message):
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    cpc_bid_micros: int
    cpc_bid_scaling_modifier: float

class CpvBidSimulationPoint(proto.Message):
    cpv_bid_micros: int
    cost_micros: int
    impressions: int
    views: int

class TargetCpaSimulationPoint(proto.Message):
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    app_installs: float
    in_app_actions: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    interactions: int
    target_cpa_micros: int
    target_cpa_scaling_modifier: float

class TargetRoasSimulationPoint(proto.Message):
    target_roas: float
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int

class PercentCpcBidSimulationPoint(proto.Message):
    percent_cpc_bid_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int

class BudgetSimulationPoint(proto.Message):
    budget_amount_micros: int
    required_cpc_bid_ceiling_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    interactions: int

class TargetImpressionShareSimulationPoint(proto.Message):
    target_impression_share_micros: int
    required_cpc_bid_ceiling_micros: int
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    absolute_top_impressions: int

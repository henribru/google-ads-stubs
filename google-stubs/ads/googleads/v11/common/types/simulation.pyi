from typing import Any

import proto

class BidModifierSimulationPoint(proto.Message):
    bid_modifier: float
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    parent_biddable_conversions: float
    parent_biddable_conversions_value: float
    parent_clicks: int
    parent_cost_micros: int
    parent_impressions: int
    parent_top_slot_impressions: int
    parent_required_budget_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        bid_modifier: float = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        parent_biddable_conversions: float = ...,
        parent_biddable_conversions_value: float = ...,
        parent_clicks: int = ...,
        parent_cost_micros: int = ...,
        parent_impressions: int = ...,
        parent_top_slot_impressions: int = ...,
        parent_required_budget_micros: int = ...
    ) -> None: ...

class BidModifierSimulationPointList(proto.Message):
    points: list[BidModifierSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[BidModifierSimulationPoint] = ...
    ) -> None: ...

class BudgetSimulationPoint(proto.Message):
    budget_amount_micros: int
    required_cpc_bid_ceiling_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        budget_amount_micros: int = ...,
        required_cpc_bid_ceiling_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...
    ) -> None: ...

class BudgetSimulationPointList(proto.Message):
    points: list[BudgetSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[BudgetSimulationPoint] = ...
    ) -> None: ...

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        required_budget_amount_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        cpc_bid_micros: int = ...,
        cpc_bid_scaling_modifier: float = ...
    ) -> None: ...

class CpcBidSimulationPointList(proto.Message):
    points: list[CpcBidSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[CpcBidSimulationPoint] = ...
    ) -> None: ...

class CpvBidSimulationPoint(proto.Message):
    cpv_bid_micros: int
    cost_micros: int
    impressions: int
    views: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        cpv_bid_micros: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        views: int = ...
    ) -> None: ...

class CpvBidSimulationPointList(proto.Message):
    points: list[CpvBidSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[CpvBidSimulationPoint] = ...
    ) -> None: ...

class PercentCpcBidSimulationPoint(proto.Message):
    percent_cpc_bid_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        percent_cpc_bid_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...
    ) -> None: ...

class PercentCpcBidSimulationPointList(proto.Message):
    points: list[PercentCpcBidSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[PercentCpcBidSimulationPoint] = ...
    ) -> None: ...

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
    target_cpa_micros: int
    target_cpa_scaling_modifier: float
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        required_budget_amount_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        app_installs: float = ...,
        in_app_actions: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        target_cpa_micros: int = ...,
        target_cpa_scaling_modifier: float = ...
    ) -> None: ...

class TargetCpaSimulationPointList(proto.Message):
    points: list[TargetCpaSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[TargetCpaSimulationPoint] = ...
    ) -> None: ...

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_impression_share_micros: int = ...,
        required_cpc_bid_ceiling_micros: int = ...,
        required_budget_amount_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        absolute_top_impressions: int = ...
    ) -> None: ...

class TargetImpressionShareSimulationPointList(proto.Message):
    points: list[TargetImpressionShareSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[TargetImpressionShareSimulationPoint] = ...
    ) -> None: ...

class TargetRoasSimulationPoint(proto.Message):
    target_roas: float
    required_budget_amount_micros: int
    biddable_conversions: float
    biddable_conversions_value: float
    clicks: int
    cost_micros: int
    impressions: int
    top_slot_impressions: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        target_roas: float = ...,
        required_budget_amount_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...
    ) -> None: ...

class TargetRoasSimulationPointList(proto.Message):
    points: list[TargetRoasSimulationPoint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        points: list[TargetRoasSimulationPoint] = ...
    ) -> None: ...

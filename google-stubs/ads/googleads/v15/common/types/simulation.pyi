from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        budget_amount_micros: int = ...,
        required_cpc_bid_ceiling_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        interactions: int = ...
    ) -> None: ...

class BudgetSimulationPointList(proto.Message):
    points: MutableSequence[BudgetSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[BudgetSimulationPoint] = ...
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    points: MutableSequence[CpcBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[CpcBidSimulationPoint] = ...
    ) -> None: ...

class CpvBidSimulationPoint(proto.Message):
    cpv_bid_micros: int
    cost_micros: int
    impressions: int
    views: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cpv_bid_micros: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        views: int = ...
    ) -> None: ...

class CpvBidSimulationPointList(proto.Message):
    points: MutableSequence[CpvBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[CpvBidSimulationPoint] = ...
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        percent_cpc_bid_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...
    ) -> None: ...

class PercentCpcBidSimulationPointList(proto.Message):
    points: MutableSequence[PercentCpcBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[PercentCpcBidSimulationPoint] = ...
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
    interactions: int
    target_cpa_micros: int
    target_cpa_scaling_modifier: float
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        required_budget_amount_micros: int = ...,
        biddable_conversions: float = ...,
        biddable_conversions_value: float = ...,
        app_installs: float = ...,
        in_app_actions: float = ...,
        clicks: int = ...,
        cost_micros: int = ...,
        impressions: int = ...,
        top_slot_impressions: int = ...,
        interactions: int = ...,
        target_cpa_micros: int = ...,
        target_cpa_scaling_modifier: float = ...
    ) -> None: ...

class TargetCpaSimulationPointList(proto.Message):
    points: MutableSequence[TargetCpaSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetCpaSimulationPoint] = ...
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    points: MutableSequence[TargetImpressionShareSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetImpressionShareSimulationPoint] = ...
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    points: MutableSequence[TargetRoasSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetRoasSimulationPoint] = ...
    ) -> None: ...

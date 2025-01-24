from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        interactions: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "budget_amount_micros",
            "required_cpc_bid_ceiling_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
            "interactions",
        ],
    ) -> bool: ...

class BudgetSimulationPointList(proto.Message):
    points: MutableSequence[BudgetSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[BudgetSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        cpc_bid_scaling_modifier: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "required_budget_amount_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
            "cpc_bid_micros",
            "cpc_bid_scaling_modifier",
        ],
    ) -> bool: ...

class CpcBidSimulationPointList(proto.Message):
    points: MutableSequence[CpcBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[CpcBidSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        views: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["cpv_bid_micros", "cost_micros", "impressions", "views"]
    ) -> bool: ...

class CpvBidSimulationPointList(proto.Message):
    points: MutableSequence[CpvBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[CpvBidSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        top_slot_impressions: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "percent_cpc_bid_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
        ],
    ) -> bool: ...

class PercentCpcBidSimulationPointList(proto.Message):
    points: MutableSequence[PercentCpcBidSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[PercentCpcBidSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        target_cpa_scaling_modifier: float = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "required_budget_amount_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "app_installs",
            "in_app_actions",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
            "interactions",
            "target_cpa_micros",
            "target_cpa_scaling_modifier",
        ],
    ) -> bool: ...

class TargetCpaSimulationPointList(proto.Message):
    points: MutableSequence[TargetCpaSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetCpaSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        absolute_top_impressions: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "target_impression_share_micros",
            "required_cpc_bid_ceiling_micros",
            "required_budget_amount_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
            "absolute_top_impressions",
        ],
    ) -> bool: ...

class TargetImpressionShareSimulationPointList(proto.Message):
    points: MutableSequence[TargetImpressionShareSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetImpressionShareSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

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
        top_slot_impressions: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "target_roas",
            "required_budget_amount_micros",
            "biddable_conversions",
            "biddable_conversions_value",
            "clicks",
            "cost_micros",
            "impressions",
            "top_slot_impressions",
        ],
    ) -> bool: ...

class TargetRoasSimulationPointList(proto.Message):
    points: MutableSequence[TargetRoasSimulationPoint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        points: MutableSequence[TargetRoasSimulationPoint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["points"]
    ) -> bool: ...

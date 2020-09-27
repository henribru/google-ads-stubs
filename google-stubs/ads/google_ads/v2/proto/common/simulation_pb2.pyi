# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Iterable as typing___Iterable, Optional as typing___Optional

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class BidModifierSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def points(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___BidModifierSimulationPoint
    ]: ...
    def __init__(
        self,
        *,
        points: typing___Optional[
            typing___Iterable[type___BidModifierSimulationPoint]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["points", b"points"]
    ) -> None: ...

type___BidModifierSimulationPointList = BidModifierSimulationPointList

class CpcBidSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def points(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CpcBidSimulationPoint
    ]: ...
    def __init__(
        self,
        *,
        points: typing___Optional[
            typing___Iterable[type___CpcBidSimulationPoint]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["points", b"points"]
    ) -> None: ...

type___CpcBidSimulationPointList = CpcBidSimulationPointList

class CpvBidSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def points(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CpvBidSimulationPoint
    ]: ...
    def __init__(
        self,
        *,
        points: typing___Optional[
            typing___Iterable[type___CpvBidSimulationPoint]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["points", b"points"]
    ) -> None: ...

type___CpvBidSimulationPointList = CpvBidSimulationPointList

class TargetCpaSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def points(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___TargetCpaSimulationPoint
    ]: ...
    def __init__(
        self,
        *,
        points: typing___Optional[
            typing___Iterable[type___TargetCpaSimulationPoint]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["points", b"points"]
    ) -> None: ...

type___TargetCpaSimulationPointList = TargetCpaSimulationPointList

class BidModifierSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def biddable_conversions(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def biddable_conversions_value(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def parent_biddable_conversions(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def parent_biddable_conversions_value(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def parent_clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def parent_cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def parent_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def parent_top_slot_impressions(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def parent_required_budget_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        biddable_conversions: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        biddable_conversions_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        clicks: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        top_slot_impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        parent_biddable_conversions: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        parent_biddable_conversions_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        parent_clicks: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        parent_cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        parent_impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        parent_top_slot_impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        parent_required_budget_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "bid_modifier",
            b"bid_modifier",
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "impressions",
            b"impressions",
            "parent_biddable_conversions",
            b"parent_biddable_conversions",
            "parent_biddable_conversions_value",
            b"parent_biddable_conversions_value",
            "parent_clicks",
            b"parent_clicks",
            "parent_cost_micros",
            b"parent_cost_micros",
            "parent_impressions",
            b"parent_impressions",
            "parent_required_budget_micros",
            b"parent_required_budget_micros",
            "parent_top_slot_impressions",
            b"parent_top_slot_impressions",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "bid_modifier",
            b"bid_modifier",
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "impressions",
            b"impressions",
            "parent_biddable_conversions",
            b"parent_biddable_conversions",
            "parent_biddable_conversions_value",
            b"parent_biddable_conversions_value",
            "parent_clicks",
            b"parent_clicks",
            "parent_cost_micros",
            b"parent_cost_micros",
            "parent_impressions",
            b"parent_impressions",
            "parent_required_budget_micros",
            b"parent_required_budget_micros",
            "parent_top_slot_impressions",
            b"parent_top_slot_impressions",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> None: ...

type___BidModifierSimulationPoint = BidModifierSimulationPoint

class CpcBidSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def biddable_conversions(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def biddable_conversions_value(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        biddable_conversions: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        biddable_conversions_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        clicks: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        top_slot_impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "impressions",
            b"impressions",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "impressions",
            b"impressions",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> None: ...

type___CpcBidSimulationPoint = CpcBidSimulationPoint

class CpvBidSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def cpv_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def views(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        cpv_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        views: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cost_micros",
            b"cost_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "impressions",
            b"impressions",
            "views",
            b"views",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cost_micros",
            b"cost_micros",
            "cpv_bid_micros",
            b"cpv_bid_micros",
            "impressions",
            b"impressions",
            "views",
            b"views",
        ],
    ) -> None: ...

type___CpvBidSimulationPoint = CpvBidSimulationPoint

class TargetCpaSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_cpa_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def biddable_conversions(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def biddable_conversions_value(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        target_cpa_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        biddable_conversions: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        biddable_conversions_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        clicks: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        top_slot_impressions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "impressions",
            b"impressions",
            "target_cpa_micros",
            b"target_cpa_micros",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "biddable_conversions",
            b"biddable_conversions",
            "biddable_conversions_value",
            b"biddable_conversions_value",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "impressions",
            b"impressions",
            "target_cpa_micros",
            b"target_cpa_micros",
            "top_slot_impressions",
            b"top_slot_impressions",
        ],
    ) -> None: ...

type___TargetCpaSimulationPoint = TargetCpaSimulationPoint

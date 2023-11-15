from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.target_frequency_time_unit import (
    TargetFrequencyTimeUnitEnum,
)
from google.ads.googleads.v13.enums.types.target_impression_share_location import (
    TargetImpressionShareLocationEnum,
)

_M = TypeVar("_M")

class Commission(proto.Message):
    commission_rate_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        commission_rate_micros: int = ...,
    ) -> None: ...

class EnhancedCpc(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ManualCpa(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ManualCpc(proto.Message):
    enhanced_cpc_enabled: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        enhanced_cpc_enabled: bool = ...,
    ) -> None: ...

class ManualCpm(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ManualCpv(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class MaximizeConversionValue(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_roas: float = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class MaximizeConversions(proto.Message):
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    target_cpa_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
        target_cpa_micros: int = ...,
    ) -> None: ...

class PercentCpc(proto.Message):
    cpc_bid_ceiling_micros: int
    enhanced_cpc_enabled: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cpc_bid_ceiling_micros: int = ...,
        enhanced_cpc_enabled: bool = ...,
    ) -> None: ...

class TargetCpa(proto.Message):
    target_cpa_micros: int
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_cpa_micros: int = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class TargetCpm(proto.Message):
    target_frequency_goal: TargetCpmTargetFrequencyGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_frequency_goal: TargetCpmTargetFrequencyGoal = ...,
    ) -> None: ...

class TargetCpmTargetFrequencyGoal(proto.Message):
    target_count: int
    time_unit: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_count: int = ...,
        time_unit: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit = ...,
    ) -> None: ...

class TargetImpressionShare(proto.Message):
    location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    location_fraction_micros: int
    cpc_bid_ceiling_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        location: TargetImpressionShareLocationEnum.TargetImpressionShareLocation = ...,
        location_fraction_micros: int = ...,
        cpc_bid_ceiling_micros: int = ...,
    ) -> None: ...

class TargetRoas(proto.Message):
    target_roas: float
    cpc_bid_ceiling_micros: int
    cpc_bid_floor_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_roas: float = ...,
        cpc_bid_ceiling_micros: int = ...,
        cpc_bid_floor_micros: int = ...,
    ) -> None: ...

class TargetSpend(proto.Message):
    target_spend_micros: int
    cpc_bid_ceiling_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        target_spend_micros: int = ...,
        cpc_bid_ceiling_micros: int = ...,
    ) -> None: ...
